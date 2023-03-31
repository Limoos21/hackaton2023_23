from django import forms


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.quiz = kwargs.pop('quiz')
        super().__init__(*args, **kwargs)
        for question in self.quiz.questions.all():
            self.fields[f'question_{question.id}'] = forms.CharField(
                label=question.features.name,
                max_length=300,
                required=True,
                widget=forms.TextInput(attrs={'class': 'form-control'}),
            )

    def clean(self):
        cleaned_data = super().clean()
        total_points = 0
        for question in self.quiz.questions.all():
            answer = cleaned_data.get(f'question_{question.id}')
            if answer and answer.lower() == question.coordinates.lower():
                total_points += question.max_points
        self.cleaned_data['total_points'] = total_points
        return cleaned_data