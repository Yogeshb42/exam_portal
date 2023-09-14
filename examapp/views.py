from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserReg, addQuestionform
from django.conf import settings
from .models import CustomUser, ExamModel, Result
from django.views.generic.base import TemplateView
from django.http import JsonResponse, HttpResponse
from django.views import View

user_model = settings.AUTH_USER_MODEL

def index(request):
    return render(request, 'index.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    
    if request.user.subject is None:
        return render(request, 'subject_unselected.html') 
    context = {
                'subject' : request.user.subject
            }

    return render(request, 'home.html', context)

def exam(request):
    if Result.objects.filter(user = request.user).exists():
        return redirect('http://localhost:8000/result')

    elif request.method == 'POST':
        questions=ExamModel.objects.filter(subject = request.user.subject)[:10]
        score=0
        wrong=0
        correct=0
        total=0
        skipped=0
        
        for q in questions:
            total+=1
            answer = request.POST.get(q.question_name)
            items = vars(q)
            try:
                print("Question :", q.question_name)
                print("User's Answer :", items[answer], "\tCorrect Answer :", q.answer)
                print()
            except KeyError:
                print("This question is skipped.")

            if answer is None:
                skipped+=1
            elif q.answer == items[answer]:
                score+=4
                correct+=1
            else:
                wrong+=1
                score-=1
        
        r = Result(user = request.user, username = request.user.username, score = score, 
                   total_questions = total, correct_anwers = correct, wrong_anwers = wrong, skipped_questions = skipped,
                   subject = request.user.subject)
        r.save()
        # return redirect('result')
        return redirect('http://localhost:8000/result')
    else:
        if request.user.subject is None:
            return render(request, 'subject_unselected.html') 
        questions=ExamModel.objects.filter(subject = request.user.subject)[:10]
        context = {
            'questions':questions
        }
        return render(request, 'exam.html',context)
    
def result(request):
    if not Result.objects.filter(user = request.user).exists():
        return redirect('http://localhost:8000/home')

    r = Result.objects.filter(user = request.user).values()
    for a in r:
        score = a['score']
        correct = a['total_questions']
        wrong = a['wrong_anwers']
        skipped = a['skipped_questions']
        total = a['total_questions']
        subject = a['subject']

    context = {
        'score':score,
        'correct':correct,
        'wrong':wrong,
        'skipped':skipped,
        'total':total,
        'subject':subject
    }
    return render(request, 'result.html',context)

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return render(request, 'home.html',)
                    return redirect('http://localhost:8000/home')
                else:
                    return render(request, 'login_user.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'login_user.html', {'error_message': 'Invalid login'})
        return render(request, 'login_user.html')
    else:
        return render(request, 'index.html')

def register_user(request):
    form = UserReg(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('http://localhost:8000/home')
    context = {
        "form": form,
    }
    return render(request, 'register_user.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def add_question(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('http://localhost:8000/add_question')
        context={'form':form}
        return render(request,'add_question.html',context)
    else: 
        # return render(request,'home.html')
        return redirect('http://localhost:8000/home')

