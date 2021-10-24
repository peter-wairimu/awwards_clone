from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Profile,Project, Review,RATE_CHOICES


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UploadProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('name','description','developer','created_date','image','linktosite')


class RateLimitForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)



