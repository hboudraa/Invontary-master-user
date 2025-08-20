from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'   # نستعمل كل الحقول من الموديل
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'raison_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raison Social'}),
            'agisant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agisant'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'phone_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Second Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fax'}),
            'nin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIN'}),
            'rip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RIP'}),
            'agence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agence'}),
            'num_rc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Num RC'}),
            'num_agriment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Num Agriment'}),
            'nif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF'}),
            'nis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIS'}),
        }
