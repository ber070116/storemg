from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    """Form to user login"""
    class Meta:
        model = User
        fields = ['username', 'password']
