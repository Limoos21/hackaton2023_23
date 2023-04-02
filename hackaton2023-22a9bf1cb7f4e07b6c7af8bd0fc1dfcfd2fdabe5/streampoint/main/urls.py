from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_quiz, name="quiz"),
    path("quize/<int:pk>", views.quiz_view, name="quiztask")
]