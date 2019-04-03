from django.contrib import admin
from core.models import Question, Answer, Star
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Star)