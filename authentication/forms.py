from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator

# Create your models here.

class SignupForm(UserCreationForm):
    username = forms.CharField(label='Email',help_text='로그인시 사용할 아이디 입력',validators=[EmailValidator()])
    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields+('email','first_name','last_name')



# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'phone', 'type')

#     # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
#     def signup(self, request, user):
#         # Save your user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()

#         # Save your profile
#         profile = Profile()
#         profile.user = user
#         profile.phone = self.cleaned_data['phone']
#         profile.type = self.cleaned_data['type']
#         profile.save()