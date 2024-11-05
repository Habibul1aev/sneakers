from django import forms
from sneakers.models import Sneakers
import re
from django.core.exceptions import ValidationError

class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ['name', 'photo', 'code', 'price', 'size', 'category', 'seazon', 'color', 'category_sneakers', 'brends']

        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}), 
            'code': forms.TextInput(attrs={'placeholder': 'Code ', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price ', 'class':'mb-2 border-b border-gray-400 outline-none pl-1'}),
        }
