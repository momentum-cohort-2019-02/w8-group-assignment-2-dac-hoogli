from django.db import models
from django.utils.text import slugify 
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date

from django.utils import timezone
from django.db import models
from core.hashids import hashids
from core.textutils import get_hashtags

import uuid
 

# Create your models here.
#Django has a built in user, so I didn't see the need to create a custom user


class Question(models.Model):
    """Model representing the intracacies of a question"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(to=User, related_name='authored_questions', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField('Date Added', auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    liked_by = models.ManyToManyField(to=User, related_name='liked_questions', blank=True)

    def __str__(self):
        return self.author.username
    # Metadata - setting order by date question is added
    class Meta: 
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)    

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        # while we can find a record already in the DB with the slug
        # we're trying to use
        while Question.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug[:50]
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs={"slug": self.slug})


class Answer(models.Model):
    """Allows logged in User to answer on a particular Question."""
    user_answer = models.TextField(null=True)
    author = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.SET_NULL, related_name="authored_answers")
    question = models.ForeignKey(to=Question, null=True, blank=True, on_delete=models.CASCADE, related_name="answers")
    answer_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    liked_by = models.ManyToManyField(to=User, related_name="liked_answers", blank=True)
    starred_at = models.DateTimeField(auto_now_add=True)
  

    class Meta:
        ordering = ['-answer_time']

    def __str__(self):
        """String for representing the string representation of object (in Admin site etc.)."""
        """thanks busyb"""
        return self.user_answer
    
    @property
    def hashid(self):
        return hashids.encode(self.pk)
    def is_starred(self):
        return self.starred_at is not None


    def mark_starred(self, save=True):
        """
        Thanks busyb
        Mark answer as starred at current time.
        Saves completion to DB until `save` is set to False.
        """
        self.starred_at = timezone.now()
        if save:
            self.save()
        return self



class Star(models.Model):
    user_star = models.ForeignKey(User, related_name='authored_stars',on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE, related_name="stars")
    

    


class AnswerQuerySet(models.QuerySet):
    def with_hashid(self, hashid):
        ids = hashids.decode(hashid)
        # TODO add check -- if len is 0, hashid is invalid, should raise exception
        if len(ids) == 1:
            return self.get(pk=ids[0])
        return self.filter(pk__in=ids)
    def notstarred(self):
        return self.filter(liked_by__isnull=True)
    def starred(self):
        return self.filter(liked_by__isnull=False)

