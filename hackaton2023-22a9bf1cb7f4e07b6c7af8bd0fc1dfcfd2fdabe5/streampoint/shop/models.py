from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField("Наименование категории", max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Geographic_Features(models.Model):
    coordinates_shir = models.CharField("Координаты широты", max_length=50)
    coordinates_dolg = models.CharField("Координаты долготы", max_length=50)
    name = models.CharField("Имя объекта", max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "географический объект"
        verbose_name_plural = "географические объекты"

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name_quiz = models.CharField("Название викторины", max_length=200)
    quiz_descriptions = models.CharField("Описание викторины", max_length=800)

    published = models.BooleanField("Публичная?")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #question = models.ForeignKey("Task", on_delete=models.CASCADE, default=1)

    points = models.IntegerField("Количество баллов", default=0)

    
    class Meta:
        verbose_name = "Викорина"
        verbose_name_plural = "Викторины"

    def __str__(self):
        return self.name_quiz

    def get_absolute_url(self):
        return reverse('shop', kwargs={'name_quiz': self.pk})



    


class Task(models.Model):
    TASK_CHOICES = [
        ('1', 'Выберите правильный географический объект'),
        ('2', 'Указать точку наиболее блюзкую к объекту'),
        ('3', 'Указать точку наиболее блюзкую к объекту'),
    ]
    task_type = models.CharField("Тип задачи", max_length=1, choices=TASK_CHOICES)
    features = models.ForeignKey(Geographic_Features, on_delete=models.CASCADE, verbose_name="Географический объект")
    coordinates_shir = models.IntegerField("Координаты пользователя", null=True)
    coordinates_dol = models.IntegerField("Координаты пользователя", null=True)
    coordinates = models.CharField("Ответ пользователя", max_length=300, null=True)
    tryy = models.IntegerField("Число попыток", default=0)
    max_points = models.IntegerField("максимальное количество баллов", default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
