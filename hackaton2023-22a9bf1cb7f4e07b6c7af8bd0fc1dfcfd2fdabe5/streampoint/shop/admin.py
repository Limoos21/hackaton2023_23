from django.contrib import admin
from .models import Quiz, Geographic_Features, Category, Task

admin.site.register(Category)
admin.site.register(Task)



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
