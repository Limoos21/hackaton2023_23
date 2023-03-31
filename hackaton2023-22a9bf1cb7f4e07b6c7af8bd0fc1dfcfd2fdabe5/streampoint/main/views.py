from django.http import HttpResponse
from django.shortcuts import render
from lkusers.models import ContribUsers
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shop.models import Quiz
from .forms import QuizForm


def show_quiz(request):
    if not request.user.is_authenticated:
        rating = ContribUsers.objects.all().order_by('-points')[:3]
        try:
            public = Quiz.objects.filter(published=True)
        except:
            public = []
        content = {"raiting": rating, 'public': public}
        return render(request, 'main/index.html', content)
    else:
        try:
            quizz = Quiz.objects.all()
        except:
            quizz = []
        rating = ContribUsers.objects.all().order_by('-points')[:3]
        content2 = {"raiting": rating, 'quizz': quizz}
        return render(request, "main/index2.html", content2)


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            total_points = form.cleaned_data['total_points']
            quiz.points = total_points
            quiz.save()
            return redirect('quiz_result', quiz_id=pk)
    else:
        form = QuizForm(quiz=quiz)
    context = {
        'form': form,
        'quiz': quiz,
    }
    return render(request, 'main/quiz_take.html', context)
