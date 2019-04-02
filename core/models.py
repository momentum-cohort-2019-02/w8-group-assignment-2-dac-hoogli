from django.db import models
from django.utils.text import slugify 
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
#Django has a built in user, so I didn't see the need to create a custom user
User = get_user_model() 

class Question(models.Model):
    """Model representing the intracacies of a question"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField('Date Added', auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True)

    # Metadata - setting order by date question is added
    class Meta: 
        ordering = ['-date_added']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('question_detail', kwargs={"slug": self.slug})

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

class Answer(models.Model):
    """Allows logged in User to answer on a particular Question."""
    user_answer = models.TextField(null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="answers")
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE, related_name="answers")
    answer_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-answer_time']

    def __str__(self):
        """String for representing the string representation of object (in Admin site etc.)."""
        return self.user_answer
