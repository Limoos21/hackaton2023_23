from django.urls import path
from . import views


urlpatterns = [
    path('', views.reg_user),
    path('login/', views.login),

]