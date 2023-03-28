from django.urls import path, re_path, include
from .views import show_profile, AddTaskall, addAddobjectsForms, QuizCreateView


urlpatterns = [
    path("", show_profile, name="Profile"),
    path("add/questions", AddTaskall, name="Task"),
    path("add/object", addAddobjectsForms, name="Objcets"),
    path("add/quiz", QuizCreateView.as_view(), name="Quize")

]

