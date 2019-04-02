from django.shortcuts import render, redirect
from core.models import Question, Answer
from .forms import QuestionForm
from django.contrib import messages
 


def index(request):

    questions = Question.objects.all()
    answers = Answer.objects.all()
    
    if request.method == "POST" and request.user.is_authenticated:
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(
                request,
                f"Thank you for your input!"
            )
            return redirect(to='index')

    form = QuestionForm()

    return render(request, 'core/index.html', context= {'answers':answers, 'questions':questions})

# Create your views here.
