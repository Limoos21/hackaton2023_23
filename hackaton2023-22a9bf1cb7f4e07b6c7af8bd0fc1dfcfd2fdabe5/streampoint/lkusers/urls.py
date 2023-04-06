from django.urls import path
from .views import show_profile, AddTaskall, addAddobjectsForms, QuizCreateView, quiz_edit, myvics,users_vics


urlpatterns = [
    path("", show_profile, name="Profile"),
    path("add/questions", AddTaskall, name="Task"),
    path("add/object", addAddobjectsForms, name="Objcets"),
    path("add/quiz", QuizCreateView.as_view(), name="Quize"),
    path("add/edit/<int:pk>", quiz_edit, name="edit"),
    path('myquiz', myvics, name="myvics"),
    path('usersvics', users_vics, name="users_vics")
]

