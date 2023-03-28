from django import forms
from shop.models import Geographic_Features, Task, Quiz


# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = ['name_quiz', 'quiz_descriptions', 'published', 'question1', 'question2',
#                   'question3']
#
#     question1 = forms.ModelMultipleChoiceField(queryset=Task1.objects.all(), widget=forms.CheckboxSelectMultiple,
#                                                required=False)
#     question2 = forms.ModelMultipleChoiceField(queryset=Task2.objects.all(), widget=forms.CheckboxSelectMultiple,
#                                                required=False)
#     question3 = forms.ModelMultipleChoiceField(queryset=Task3.objects.all(), widget=forms.CheckboxSelectMultiple,
#                                                required=False)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_type', 'features', 'coordinates_shir', 'coordinates_dol', 'coordinates', 'tryy',
                  'max_points']

TaskFormSet = forms.modelformset_factory(Task, form=TaskForm, extra=1)

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name_quiz', 'quiz_descriptions', 'published', 'user', 'points']

    tasks = TaskFormSet(queryset=Task.objects.none(), prefix='task')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tasks'] = TaskFormSet(queryset=self.instance.question.all(), prefix='task')
        elif 'data' in kwargs:
            self.fields['tasks'] = TaskFormSet(queryset=Task.objects.none(), prefix='task', data=kwargs['data'])

    def save(self, commit=True):
        quiz = super().save(commit)
        if commit:
            tasks = self.cleaned_data['tasks'].save(commit=False)
            for task in tasks:
                task.save()
                quiz.question.add(task)
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
