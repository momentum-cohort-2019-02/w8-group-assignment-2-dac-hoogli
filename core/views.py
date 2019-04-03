from django.shortcuts import render, redirect
from core.models import Question, Answer, Star
from .forms import QuestionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
 


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


def question_detail(request, slug):
    question = Question.objects.get(slug=slug)
    answers = question.answers.all() 
    return render(request, 'core/question_detail.html', context={'question': question, 'answers':answers})

def profile(request, username):
    user = User.objects.get(username=username)
    questions = user.authored_questions.all() 

    # paginator = Paginator(posts, 20)
    # page = request.GET.get('page', 1)
    # posts = paginator.get_page(page)

    return render(request, 'core/profile_page.html', context={'user': user, 'questions': questions})

def add_answer(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question 
            answer.save()
            return redirect('question_detail', slug=post.slug)
   
    form = AnswerForm()
    template = 'core/add_answer.html'
    context = {'form': form, 'question': question }

    return render(request, template, context)
    
@login_required
def like_question(request, slug):
    question = Question.objects.get(slug=slug)
    if request.user not in question.liked_by.all():
        question.liked_by.add(request.user)
    else:
        question.liked_by.remove(request.user)
    return redirect(to='index')

@login_required
def delete_question(request, slug):
    question = Question.objects.get(slug=slug)
    question.delete()
    return redirect(to='index')

