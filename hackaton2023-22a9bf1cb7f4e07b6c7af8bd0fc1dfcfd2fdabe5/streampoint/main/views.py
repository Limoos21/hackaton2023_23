from django.http import HttpResponse
from django.shortcuts import render
from lkusers.models import ContribUsers, History
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from shop.models import Quiz, Task
from .forms import ContribUserForm, HistoryForm
from math import *


def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance1 = R * c
    distance = round(distance1, 2)

    return distance


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
    taskss = Task.objects.filter(quizzes=pk)
    user = ContribUsers.objects.get(user_id=request.user.id)
    points_his = 0
    if request.method == "POST":
        form = ContribUserForm(request.POST, instance=user)
        try:
            quizzz = History.objects.get(quiz_id=pk)
            form2 = HistoryForm(request.POST, instance=quizzz)
        except:
            form2 = HistoryForm(request.POST)
        task_id = request.POST.get('task_id')
        coordinates_shir = request.POST.get('coordinates_shir{}'.format(task_id))
        coordinates_dol = request.POST.get('coordinates_dol{}'.format(task_id))
        coordinates = request.POST.get('coordinates{}'.format(task_id))

        if form.is_valid() and form2.is_valid():
            tasks = Task.objects.get(id=task_id)
            if tasks.features.name == coordinates:
                points_his += tasks.max_points
            else:
                points_his += 0

            try:
                dists = calculate_distance(float(coordinates_dol), float(coordinates_shir),
                                           float(tasks.features.coordinates_dolg),
                                           float(tasks.features.coordinates_shir))
                if dists > 100:
                    points_his += 0
                else:
                    d = (100 - dists) / 100
                    points_his += tasks.max_points * d
            except:
                points_his += 0

            history = form2.save(commit=False)
            points = form.save(commit=False)
            history.user_id = request.user.id
            history.quiz_id = pk
            history.points += points_his
            points.points += points_his

            points.save()
            history.save()
            return redirect(request.path_info)

        else:
            # Return the page with the form and error messages
            return render(request, "main/quiz_take.html", {"quiz": quiz, "tasks": taskss, "form1": form,
                                                           "form2": form2})
    else:
        form = ContribUserForm()
        form2 = HistoryForm()
        return render(request, 'main/quiz_take.html', {"quiz": quiz, "tasks": taskss, "form1": form, "form2": form2})
