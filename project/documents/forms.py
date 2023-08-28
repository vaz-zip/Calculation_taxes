from django import forms
from .models import Document
from django.contrib.auth.models import User


class DocumentCreateForm(forms.ModelForm):
    images = forms.ImageField(label='Фото документа', widget=forms.ClearableFileInput(attrs={'multiple': True, "class":"mybottom"}))
    class Meta:
        model = Document
        widgets = {'dateCreate': forms.DateInput(attrs={'type': 'date'}), }
        fields = ['title', 'category', 'textDocument', 'number', 'dateCreate', 'images']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        widgets = {'dateCreate': forms.DateInput(attrs={'type': 'date'}), }
        fields = ['title', 'slug', 'category', 'textDocument', 'number', 'dateCreate']