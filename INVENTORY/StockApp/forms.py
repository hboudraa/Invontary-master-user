from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'quantity', 'price']  # Define the fields you want in the form

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter name of product here ...'
        self.fields['name'].label = 'Enter name of product: '
        self.fields['category'].label = 'Enter category of product: '
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['placeholder'] = 'Enter category of product here ...'
        self.fields['quantity'].label = 'Enter quantity of product: '
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter quantity of product here ...'
        self.fields['price'].label = 'Enter Price: '
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter price of product here ...'

class EnterForm(forms.ModelForm):
    class Meta:
        model = FicheStockEntr
        fields = ['number', 'source', 'quantity', 'price', 'observation']

    def __init__(self, *args, product=None,**kwargs):
        super(EnterForm, self).__init__(*args, **kwargs)
        if product:
            self.instance.name_fiche = product  # تعيين اسم المنتج تلقائيًا
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['placeholder'] = 'Enter number of fiche here ...'
        self.fields['source'].widget.attrs['class'] = 'form-control'
        self.fields['source'].widget.attrs['placeholder'] = 'Enter name of source here ...'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter name of quantity here ...'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter name of price here ...'

class SortieForm(forms.ModelForm):
    class Meta:
        model = FicheStockSortie
        fields = ['number', 'destination', 'quantity', 'observation']

    def __init__(self, *args, product=None,**kwargs):
        super(SortieForm, self).__init__(*args, **kwargs)
        if product:
            self.instance.name_fiche = product  # تعيين اسم المنتج تلقائيًا
        self.fields['number'].widget.attrs['class'] = 'form-control'
        self.fields['number'].widget.attrs['placeholder'] = 'Enter number of fiche here ...'
        self.fields['destination'].widget.attrs['class'] = 'form-control'
        self.fields['destination'].widget.attrs['placeholder'] = 'Enter name of destination here ...'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter name of quantity here ...'

class DemandClassForm(forms.ModelForm):
    
    class Meta:
        model = DemandClass
        fields = ('quantity',)

    def __init__(self, *args, product=None,**kwargs):
        super(DemandClassForm, self).__init__(*args, **kwargs)
        if product:
            self.instance.name_demand = product  # تعيين اسم المنتج تلقائيًا

        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Enter quantity of product do you want here ...'

