from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'total_points']
        labels = {
            'name': 'Member Name',
            'email': 'Email Address',
        }
        help_texts = {
            'email': 'Please enter a valid email address.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['total_points'].disabled = True
