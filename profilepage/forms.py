from django import forms

from .models import Profile, Contact

class ProfileForm(forms.ModelForm):
    """
    A class for the profile update form
    """

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date']


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields = ['name', 'email', 'message']

 
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Your message'
                }
            )
        }

    