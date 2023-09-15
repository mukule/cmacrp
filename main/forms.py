# forms.py

from django import forms
from .models import Business, Company, Document

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'business']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'business': forms.Select(attrs={'class': 'form-control'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'company']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }
