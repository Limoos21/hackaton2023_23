from django import forms
from django.db.models import Sum
from shop.models import Geographic_Features, Task, Quiz, Category


class QuizForm(forms.ModelForm):
    class QuestionWidget(forms.CheckboxSelectMultiple):
        def init(self, attrs=None, *args, **kwargs):
            super().init(attrs, args, kwargs)

        def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
            option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
            task = self.choices.queryset[index]
            option['label'] = f'{task.features.name} ({task.get_task_type_display()}) - {task.max_points} points'
            return option

    # добавить классы CSS к каждому полю формы
    name_quiz = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-quiz'}))
    quiz_descriptions = forms.CharField(widget=forms.Textarea(attrs={'class': 'desc-text'}))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'quiz-published', 'class': 'quiz-field'}))
    questions = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), widget=QuestionWidget(attrs={'class': 'quiz-que'}))
    photo_quiz = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'quiz-photo'}))

    class Meta:
        model = Quiz
       
        fields = ['name_quiz', 'quiz_descriptions', 'published', 'questions', 'photo_quiz']
        label = {'quiz_descriptions': 'Описание'}

    def init(self, *args, kwargs):
        super().init(*args, **kwargs)
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


class AddTask1Forms(forms.ModelForm):
    task_type = forms.ChoiceField(choices=Task.TASK_CHOICES, widget=forms.RadioSelect(attrs={'class': 'type'}))
    features = forms.ModelChoiceField(queryset=Geographic_Features.objects.all(), widget=forms.Select(attrs={'class': 'point'}))
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'desc-text', 'rows': 3}))
    max_points = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'max-ball'}))
    class Meta:
        model = Task
        fields = ("task_type", "features", "question", "max_points")





class Geographic_FeaturesForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-quiz'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),  widget=forms.Select(attrs={'class': 'point'}))
                                     
    class Meta:
        model = Geographic_Features
        fields = ["category", "name"]

