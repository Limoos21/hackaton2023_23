from django.conf import settings
from .models import History, ContribUsers
from shop.models import Quiz
from django.shortcuts import render
from .forms import AddobjectsForms, AddTask3Forms, AddTask2Forms, AddTask1Forms, QuizeForms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def addquiz(request):
    user_id = request.user.id
    if request.method == "POST":
        form = QuizeForms(request.POST, request.FILES)
        if form.is_valid():
            addproduct = form.save(commit=False)
            addproduct.streamer_id = id_stream
            try:
                form.save()
                return redirect("myshopp")
            except:
                form.add_error(None, "Ошибка добавления товара")
    else:
        form = AddproductForms()
    return render(request, "profile/addproduct.html", {"form": form})




@login_required
def addAddobjectsForms(request):
    if request.method == "POST":
        form = AddobjectsForms(request.POST)
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
        form = AddobjectsForms()
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
