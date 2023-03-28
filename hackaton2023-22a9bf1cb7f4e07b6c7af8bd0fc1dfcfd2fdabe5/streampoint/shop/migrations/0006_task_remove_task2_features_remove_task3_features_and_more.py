# Generated by Django 4.1.5 on 2023-03-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_user_quiz_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('1', 'Выберите правильный географический объект'), ('2', 'Указать точку наиболее блюзкую к объекту'), ('3', 'Указать точку наиболее блюзкую к объекту')], max_length=1, verbose_name='Тип задачи')),
                ('coordinates_shir', models.IntegerField(null=True, verbose_name='Координаты пользователя')),
                ('coordinates_dol', models.IntegerField(null=True, verbose_name='Координаты пользователя')),
                ('coordinates', models.CharField(max_length=300, null=True, verbose_name='Ответ пользователя')),
                ('tryy', models.IntegerField(default=0, verbose_name='Число попыток')),
                ('max_points', models.IntegerField(default=0, verbose_name='максимальное количество баллов')),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.geographic_features', verbose_name='Географический объект')),
            ],
        ),
        migrations.RemoveField(
            model_name='task2',
            name='Features',
        ),
        migrations.RemoveField(
            model_name='task3',
            name='Features',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question3',
        ),
        migrations.DeleteModel(
            name='Task1',
        ),
        migrations.DeleteModel(
            name='Task2',
        ),
        migrations.DeleteModel(
            name='Task3',
        ),
        migrations.AddField(
            model_name='task',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.quiz'),
        ),
    ]
