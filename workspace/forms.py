from django import forms
from sneakers.models import Sneakers
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
import re
from django.core.exceptions import ValidationError

class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ['name', 'photo', 'code', 'price', 'size', 'category', 'seazon', 'color', 'category_sneakers', 'brends']

        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black mb-3 text-red-500"}), 
            'code': forms.TextInput(attrs={'placeholder': 'Code ', 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500"}),
            'price': forms.TextInput(attrs={'placeholder': 'Price ', 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500"}),
            'size': forms.SelectMultiple(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500'}),
            'category': forms.Select(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500'}),
            'seazon': forms.Select(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500'}),
            'color': forms.Select(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500'}),
            'category_sneakers': forms.Select(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black text-red-500'}),
            'brends': forms.Select(attrs={'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black mb-3 text-red-500'}),

        }


class LoginForm(forms.Form):
    user = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'w-full p-3 mb-2 border border-[#ccc] rounded-md text-base bg-white focus:border-[#007bff] focus:outline-none transition-colors duration-300'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'w-full p-3 mb-4 border border-[#ccc] rounded-md text-base bg-white focus:border-[#007bff] focus:outline-none transition-colors duration-300'}))


class RegisterForm(BaseUserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Введите пароль", 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Подтвердите пароль", 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets={
            'username': forms.TextInput(attrs={'placeholder':"Введите ваше имя", 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"}),
            'email': forms.EmailInput(attrs={'placeholder':"Введите ваш email", 'class':"w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-black"}),
        }

    
    

