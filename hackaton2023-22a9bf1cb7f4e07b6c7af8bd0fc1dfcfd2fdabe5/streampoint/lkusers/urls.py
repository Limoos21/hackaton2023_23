from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path("", views.show_profile, name="Profile"),
    path("add/questions", views.AddTaskall, name="Task"),
    path("add/object", views.addAddobjectsForms, name="Objcets"),
    path("add/quiz", views.create_quiz, name="Quize")

]

