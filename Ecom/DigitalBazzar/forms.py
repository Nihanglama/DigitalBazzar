import imp
from statistics import mode
from django.db.models import fields
from django.db.models.fields import Field
from .models import Shipping
from django.forms import ModelForm, forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Ship_form(ModelForm):
    class Meta:
        model=Shipping
        fields='__all__'
        exclude=('customer','order')

class Signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



