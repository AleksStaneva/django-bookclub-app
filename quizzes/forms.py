from django import forms
from .models import QuizResult


class QuizResultForm(forms.ModelForm):
    class Meta:
        model = QuizResult
        fields = ['score']
        labels = {
            'score': 'Your Score',
        }

    def clean_score(self):
        score = self.cleaned_data['score']
        if score < 0:
            raise forms.ValidationError(
                'Score cannot be negative.'
            )
        return score
