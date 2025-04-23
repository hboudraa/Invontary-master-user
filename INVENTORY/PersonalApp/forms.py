from django import forms
from .models import *


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['name_french', 'phone', 'phone_2', 'fax', 'email', 'nin', 'rip', 'recruitment']
    def __init__(self, *args, **kwargs):
        super(UtilisateurForm, self).__init__(*args, **kwargs)
        self.fields['name_french'].widget.attrs['class'] = 'form-control'
        self.fields['name_french'].widget.attrs['placeholder'] = 'Enter name of Person here ...'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone number of Person here ...'
        self.fields['phone_2'].widget.attrs['class'] = 'form-control'
        self.fields['phone_2'].widget.attrs['placeholder'] = 'If there is Another Number Phone'
        self.fields['fax'].widget.attrs['class'] = 'form-control'
        self.fields['fax'].widget.attrs['placeholder'] = 'Enter fax of Person here ...'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email of Person here ...'
        self.fields['nin'].widget.attrs['class'] = 'form-control'
        self.fields['nin'].widget.attrs['placeholder'] = 'Enter nin of Person here ...'
        self.fields['rip'].widget.attrs['class'] = 'form-control'
        self.fields['rip'].widget.attrs['placeholder'] = 'Enter rip of Person here ...'
        self.fields['recruitment'].widget.attrs['class'] = 'form-control'
        self.fields['recruitment'].widget.attrs['placeholder'] = 'Enter recruitment of Person here ...'
