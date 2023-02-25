from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User_book
        fields = ['name', 'email']


class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBook
        fields = ['user', 'title', 'description', 'status', 'important']