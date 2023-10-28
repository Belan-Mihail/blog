from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    """
    A class for the profile update form
    """

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your name'})
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message', 'class': 'feedback'})
    )
