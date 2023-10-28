from django import forms

from .models import Profile

class ProfileForm(forms.ModelForm):
    """
    A class for the profile update form
    """

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']

