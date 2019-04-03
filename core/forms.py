from django import forms
from core.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'author', 'description')
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('author', 'user_answer')
        