from django import forms
import re
from django.contrib.auth.models import User



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    ten = forms.CharField(max_length=30)
    
