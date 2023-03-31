from django import forms
from django.db.models import Sum
from shop.models import Geographic_Features, Task, Quiz


class QuizForm(forms.ModelForm):
    class QuestionWidget(forms.CheckboxSelectMultiple):
        def __init__(self, attrs=None, *args, **kwargs):
            super().__init__(attrs, *args, **kwargs)

        def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
            option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
            task = self.choices.queryset[index]
            option['label'] = f'{task.features.name} ({task.get_task_type_display()}) - {task.max_points} points'
            return option

    questions = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), widget=QuestionWidget())

    class Meta:
        model = Quiz
        fields = ['name_quiz', 'quiz_descriptions', 'published', 'questions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = self.instance.questions.all()

    def save(self, commit=True):
        quiz = super().save(commit=False)
        if commit:
            quiz.save()
            self.save_m2m()
            quiz.points = quiz.questions.aggregate(total_points=Sum('max_points'))['total_points']
            quiz.save()
        return quiz





# class AddTask1Forms(forms.ModelForm):
#     class Meta:
#         model = Task1
#         fields = ("task", "Features", "tryy", "max_points")
#
#
# class AddTask2Forms(forms.ModelForm):
#     class Meta:
#         model = Task2
#         fields = ("task", "Features", "max_points")
#
#
# class AddTask3Forms(forms.ModelForm):
#     class Meta:
#         model = Task3
#         fields = ("task", "Features", "max_points", "max_points")


class Geographic_FeaturesForms(forms.ModelForm):
    class Meta:
        model = Geographic_Features
        fields = ["category", "name"]

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
