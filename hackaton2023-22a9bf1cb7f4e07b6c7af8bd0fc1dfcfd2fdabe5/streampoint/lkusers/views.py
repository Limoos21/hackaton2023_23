from django.conf import settings
from django.db.models import Sum
from .models import History, ContribUsers
from shop.models import Quiz, Task
from .forms import QuizForm, Geographic_FeaturesForms, AddTask1Forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404


def quiz_edit(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            quiz = form.save()
            quiz.points = quiz.questions.aggregate(total_points=Sum('max_points'))['total_points']
            quiz.save()
            return redirect('Profile')
    else:
        form = QuizForm(instance=quiz)

    context = {
        'form': form,
        'quiz': quiz,
        'question_data': [(question.task_type, question.max_points, question.features) for question in
                          Task.objects.all()],
    }

    return render(request, 'profile/quiz_edit.html', context)

class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'profile/Quiz.html'
    success_url = reverse_lazy('Profile')

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.user = self.request.user
        quiz.extra_info = 'Some additional info'
        quiz.photo_quiz = self.request.FILES.get('photo_quiz')
        quiz.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_data'] = [(question.task_type, question.max_points, question.features) for question in
                                    Task.objects.all()]
        return context
# class QuizCreateView(CreateView):
#     model = Quiz
#     form_class = QuizForm
#     template_name = 'profile/Quiz.html'
#     success_url = reverse_lazy('Profile')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['question_data'] = [(question.task_type, question.max_points, question.features) for question in
#                                     Task.objects.all()]
#         return context


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

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
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
    task = Task.objects.all()
    if request.method == "POST":
        form1 = AddTask1Forms(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect(request.path_info)
    else:
        form1 = AddTask1Forms()
    return render(request, "profile/addtaskall.html", {"form1": form1, "task": task})


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


def myvics(request):
    try:
        his_quiz = Quiz.objects.filter(user_id=request.user.id)
    except:
        his_quiz = []

    return render(request, 'profile/myvics.html', {"his_quiz": his_quiz})


def users_vics(request):
    try:
        his_quiz = Quiz.objects.all()
    except:
        his_quiz = []

    return render(request, 'profile/users_vics.html', {"all_quiz": his_quiz})