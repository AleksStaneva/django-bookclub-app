from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'month_selected', 'author']
        labels = {
            'title': 'Book Title',
            'description': 'Short Description',
            'month_selected': 'Month Selection',
            'author': 'Author',
        }
        help_texts = {
            'month_selected': 'Example: February 2026',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_month_selected(self):
        month = self.cleaned_data['month_selected']
        if len(month) < 3:
            raise forms.ValidationError(
                'Month name is too short.'
            )
        return month
