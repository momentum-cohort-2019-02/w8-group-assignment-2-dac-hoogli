from django.shortcuts import render
from core.models import Question, Answer

def index(request):

    questions = Question.objects.all()
    answers = Answer.objects.all()

    return render(request, 'core/index.html', context= {'answers':answers, 'questions':questions})

# Create your views here.
