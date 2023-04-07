# Generated by Django 4.2 on 2023-04-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Geographic_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates_shir', models.DecimalField(decimal_places=5, max_digits=50, verbose_name='Координаты широты')),
                ('coordinates_dolg', models.DecimalField(decimal_places=5, max_digits=50, verbose_name='Координаты долготы')),
                ('name', models.CharField(max_length=250, verbose_name='Имя объекта')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category')),
            ],
            options={
                'verbose_name': 'географический объект',
                'verbose_name_plural': 'географические объекты',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=200, null=True, verbose_name='Напишите вопрос')),
                ('task_type', models.CharField(choices=[('1', 'Выберите правильный географический объект'), ('2', 'Указать точку наиболее близкую к объекту'), ('3', 'Напишите название географического объекта, который указан на карте')], max_length=1, verbose_name='Тип задачи')),
                ('coordinates_shir', models.DecimalField(decimal_places=5, default=1.0, max_digits=50, null=True, verbose_name='Координаты пользователя')),
                ('coordinates_dol', models.DecimalField(decimal_places=5, default=1.0, max_digits=50, null=True, verbose_name='Координаты пользователя')),
                ('coordinates', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ответ пользователя')),
                ('tryy', models.IntegerField(default=1, verbose_name='Число попыток')),
                ('max_points', models.IntegerField(default=0, verbose_name='максимальное количество баллов')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.geographic_features', verbose_name='Географический объект')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_quiz', models.ImageField(blank=True, help_text='фото викторины', null=True, upload_to='photoquiz/', verbose_name='Картинка викторины')),
                ('name_quiz', models.CharField(max_length=200, verbose_name='Название викторины')),
                ('quiz_descriptions', models.CharField(max_length=800, verbose_name='Описание викторины')),
                ('published', models.BooleanField(verbose_name='Публичная?')),
                ('points', models.IntegerField(default=0, verbose_name='Количество баллов')),
                ('questions', models.ManyToManyField(related_name='quizzes', to='shop.task', verbose_name='Вопросы')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Викорина',
                'verbose_name_plural': 'Викторины',
            },
        ),
    ]