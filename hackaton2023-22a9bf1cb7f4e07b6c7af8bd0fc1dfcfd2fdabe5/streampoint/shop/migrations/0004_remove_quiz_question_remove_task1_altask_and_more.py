# Generated by Django 4.1.7 on 2023-03-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alltask_alter_geographic_features_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.RemoveField(
            model_name='task1',
            name='altask',
        ),
        migrations.RemoveField(
            model_name='task2',
            name='altask',
        ),
        migrations.RemoveField(
            model_name='task3',
            name='altask',
        ),
        migrations.AddField(
            model_name='quiz',
            name='question1',
            field=models.ManyToManyField(default=1, to='shop.task1'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question2',
            field=models.ManyToManyField(default=1, to='shop.task2'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question3',
            field=models.ManyToManyField(default=1, to='shop.task3'),
        ),
        migrations.DeleteModel(
            name='Alltask',
        ),
    ]
