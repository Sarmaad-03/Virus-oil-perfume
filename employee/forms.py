from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from employee.models import Employee

class UserForm(UserCreationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"username"}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':"password"}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':"password confirmation"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EmployeeForm(forms.ModelForm):

    first_name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите имя"}))
    last_name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите фамилию"}))
    number = forms.IntegerField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':"введите номер"}))
    bithday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control date-picker', 'placeholder':"введите дату"}))

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'number', 'bithday')