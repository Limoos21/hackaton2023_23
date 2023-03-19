from django.conf import settings
from .models import History, ContribUsers
from shop.models import Quiz
from django.shortcuts import render
from .forms import AddTask3Forms, AddTask2Forms, AddTask1Forms, QuizForm, Geographic_FeaturesForms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user_id = request.user.id

            # Вычисляем сумму баллов из связанных объектов Task
            max_points = 0
            for question in ['question1', 'question2', 'question3']:
                for task in form.cleaned_data[question]:
                    max_points += task.max_points

            quiz.points = max_points
            quiz.save()
            form.save_m2m()  # сохраняем ManyToMany поля
            return redirect('Profile')
    else:
        form = QuizForm()
    return render(request, 'profile/Quiz.html', {'form': form})




@login_required
def addAddobjectsForms(request):
    if request.method == "POST":
        form = Geographic_FeaturesForms(request.POST)
        if form.is_valid():
            # Создаем объект модели на основе данных формы и сохраняем его в базу данных
            addobject = form.save(commit=False)
            addobject.coordinates_shir = request.POST.get('coordinates_shir')
            addobject.coordinates_dolg = request.POST.get('coordinates_dolg')
            addobject.save()
            return redirect("Profile")
        else:
            # Возвращаем страницу с формой и сообщениями об ошибках
            return render(request, "profile/addquiz.html", {"form": form})
    else:
        form = Geographic_FeaturesForms()
    return render(request, "profile/addquiz.html", {"form": form})





@login_required
def AddTaskall(request):
    if request.method == "POST":
        form1 = AddTask1Forms(request.POST)
        form2 = AddTask2Forms(request.POST)
        form3 = AddTask3Forms(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form3.save()
            form1.save()
            form2.save()
    else:
        form1 = AddTask1Forms()
        form2 = AddTask2Forms()
        form3 = AddTask3Forms()
    return render(request, "profile/addtaskall.html", {"form1": form1, "form2": form2, "form3": form3})


def show_profile(request):
    user_id = request.user.id
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    elif request.user.is_superuser:
        name = ContribUsers.objects.get(id=user_id)
        try:
            all_quiz = Quiz.objects.all()
        except:
            all_quiz = []
        try:
            history = History.objects.all()
        except:
            history = []
        try:
            his_history = History.objects.filter(user=user_id)
        except:
            his_history = []
        return render(request, "profile/profile.html", {"name": name, "history": history, "all_quiz": all_quiz,
                                                        "his_history": his_history})
    else:
        name = ContribUsers.objects.get(id=user_id)
        try:
            his_quiz = Quiz.objects.all()
        except:
            his_quiz = []
        try:
            his_history = History.objects.filter(user=user_id)
        except:
            his_history = []
        return render(request, "profile/profileuser.html", {"name": name, "his_quiz": his_quiz,
                                                            "his_history": his_history})
