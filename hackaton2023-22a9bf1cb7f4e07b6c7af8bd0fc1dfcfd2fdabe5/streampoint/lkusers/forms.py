from django import forms
from shop.models import Geographic_Features, Task1, Task2, Task3, Quiz
class AddobjectsForms(forms.ModelForm):
    class Meta:
        model = Geographic_Features
        fields = ("name", "category")



class AddTask1Forms(forms.ModelForm):
    class Meta:
        model = Task1
        fields = ("task", "Features", "tryy", "max_points")


class AddTask2Forms(forms.ModelForm):
    class Meta:
        model = Task2
        fields = ("task", "Features", "max_points")



class AddTask3Forms(forms.ModelForm):
    class Meta:
        model = Task3
        fields = ("task", "Features", "max_points", "max_points")


class QuizeForms(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ("name_quiz", "quiz_descriptions", "published")





# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = ['name_quiz', 'quiz_descriptions', 'published']
#
#     Geographic_FeaturesFormSet = inlineformset_factory(
#         Quiz,
#         Geographic_Features,
#         fields=('question', 'coordinates_shir', 'coordinates_dolg', 'name', 'category', 'max_points'),
#         extra=15,
#         can_delete=True,  # чтобы можно было удалить уже существующие вопросы
#         min_num=1,  # минимальное количество вопросов
#         validate_min=True,
#     )


