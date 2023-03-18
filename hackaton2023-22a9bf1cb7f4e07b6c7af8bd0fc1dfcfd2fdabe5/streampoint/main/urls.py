from django.urls import path
from . import views


urlpatterns = [
    # path('', views.show_profile),
    path('quize/', views.show_quiz, name="quiz")
]