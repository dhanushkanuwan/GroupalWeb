from models import ContactGroup, UserProfile
from django.forms import ModelForm, Textarea
from django import forms

class ContactGroupForm(ModelForm):
    class Meta:
        model = ContactGroup
        fields = ['name', 'title', 'description', 'thumbnail']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 5})
        }


class UserProfileForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data

    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name']