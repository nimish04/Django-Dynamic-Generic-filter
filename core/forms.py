from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django_filters
from .models import *

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username=forms.CharField(max_length=100,min_length=3,required=True)
    # mobile=forms.CharField(min_length=10,required=False)
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        # fields = ('first_name', 'last_name','username','mobile' ,'email', 'password1', 'password2' )
        fields=('username','email')

class ForgotPasswordForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text="Required. Inform a valid email address.")
    class Meta:
        model=User
        fields=('email',)

class ChangePasswordForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text="Required. Inform a valid email address.")
    old_password=forms.CharField(max_length=100,required=True)
    new_password=forms.CharField(max_length=100,required=True)
    class Meta:
        model=User
        fields=('email','old_password','new_password')


class Packageip(forms.ModelForm):
	package=Package.objects.all()
	attributes=PackageAttribute.objects.all()

	class Meta :
		model=Package
		fields=('name','description','attributes')
