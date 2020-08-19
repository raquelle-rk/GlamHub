from django import forms
# from django.forms import ModelForm

from review.models import Review


class ReviewForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Leave a review'}),
        label=False)

    class Meta:
        model = Review
        fields = ('body',)
