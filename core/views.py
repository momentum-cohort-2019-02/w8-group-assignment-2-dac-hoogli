from django.shortcuts import render, redirect
from core.models import Question, Answer, Star
from .forms import QuestionForm, AnswerForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator




def index(request):

    questions = Question.objects.all()
    answers = Answer.objects.all()
    
    if request.method == "POST":
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
    paginator = Paginator(questions, 10)
    page = request.GET.get('page', 1)
    questions = paginator.get_page(page)

    return render(request, 'core/index.html', context= {'answers':answers, 'questions':questions, 'form':form })


def question_detail(request, slug):
    question = Question.objects.get(slug=slug)
    answers = question.answers.all() 
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question 
            answer.save()
            return redirect('question_detail', slug=question.slug)
   
    form = AnswerForm()
    return render(request, 'core/question_detail.html', context = {'form': form, 'question': question, 'answers': answers })

def profile(request, username):
    user = User.objects.get(username=username)
    questions = user.authored_questions.all() 

    # paginator = Paginator(posts, 20)
    # page = request.GET.get('page', 1)
    # posts = paginator.get_page(page)

    return render(request, 'core/profile_page.html', context={'user': user, 'questions': questions})
    
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


# thanks busyb
@require_http_methods(['POST'])
@login_required
def mark_answer_starred(request, answer_id):
    answer = request.user.answers.with_hashid(answer_id)
    if answer is None:
        raise Http404('No answer matches the given query.')
    answer.answer_starred()
    if request.is_ajax():
        return JsonResponse({"id": answer.hashid, "starred": True})
    return redirect('question_detail')

