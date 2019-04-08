from django import forms
from core.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # exclude = ['date_added', 'slug', 'liked_by']
        fields = ['title', 'author', 'description']
        # widgets = {
        #     'description': forms.TextInput(attrs={
        #         'id': 'questionForm',
        #         'required': True,
        #         'placeholder': 'pose a question'
        #     })

        # }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('author', 'user_answer')

    