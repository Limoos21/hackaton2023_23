from django.conf import settings
from .models import History, ContribUsers
from shop.models import Quiz, Task
from django.shortcuts import render
from .forms import TaskForm, QuizForm, Geographic_FeaturesForms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.forms import inlineformset_factory



class QuizCreateView(CreateView):
    model = Quiz
    template_name = 'profile/Quiz.html'
    fields = ['name_quiz', 'quiz_descriptions', 'published', 'user', 'points']
    success_url = reverse_lazy('quiz_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['tasks'] = TaskFormSet(self.request.POST)
        else:
            data['tasks'] = TaskFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        tasks = context['tasks']
        form.instance.user = self.request.user
        self.object = form.save()
        if tasks.is_valid():
            tasks.instance = self.object
            tasks.save()
        return super().form_valid(form)


TaskFormSet = inlineformset_factory(Quiz, Task, fields=('task_type', 'features', 'coordinates_shir', 'coordinates_dol', 'coordinates', 'tryy', 'max_points'), extra=1, can_delete=True)



# @login_required
# def create_quiz(request):
#     if request.method == 'POST':
#         form = QuizForm(request.POST)
#         if form.is_valid():
#             quiz = form.save(commit=False)
#             quiz.user_id = request.user.id
#
#             # Вычисляем сумму баллов из связанных объектов Task
#             max_points = 0
#             for question in ['question1', 'question2', 'question3']:
#                 for task in form.cleaned_data[question]:
#                     max_points += task.max_points
#
#             quiz.points = max_points
#             quiz.save()
#             form.save_m2m()  # сохраняем ManyToMany поля
#             return redirect('Profile')
#     else:
#         form = QuizForm()
#     return render(request, 'profile/Quiz.html', {'form': form})




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


def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    lat1 = [0.0]
    lon1 = [0.0]
    lat2 = Geographic_Features.objects('coordinates_shir')
    lon2 = Geographic_Features.objects('coordinates_dolg')
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print(distance)
    return print(distance)


def map_view(request):
    # Создание объекта карты
    my_map = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Добавление маркера на карту
    folium.Marker(
        location=[45.5236, -122.6750],
        popup='Portland, OR',
        icon=folium.Icon(color='green')
    ).add_to(my_map)

    # Добавление кругового маркера на карту
    folium.Circle(
        location=[45.5215, -122.6261],
        radius=500,
        popup='Laurelhurst Park',
        color='crimson',
        fill=False,
    ).add_to(my_map)

    # Конвертация карты в HTML
    my_map = my_map._repr_html_()

    return my_map



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
