from django.contrib import admin
from .models import Quiz, Geographic_Features, Category, Task1, Task2, Task3

admin.site.register(Category)
admin.site.register(Task2)
admin.site.register(Task3)
admin.site.register(Task1)



@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ("name_quiz", "quiz_descriptions", "published")
    list_filter = ["user_id"]


@admin.register(Geographic_Features)
class Geographic_Features(admin.ModelAdmin):
    list_display = ("coordinates_shir", "coordinates_dolg", "name")
    list_filter = ["category"]

    class Meta:
        verbose_name = "Геграфические объекты"
