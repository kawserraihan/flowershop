from django import forms
from .models import *

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description', 'image']

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description', 'image']


class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description', 'image']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','contact','address']

class TypeForm(forms.ModelForm):
    class Meta:
        model = type
        fields = ['name',]

class ColorForm(forms.ModelForm):
    class Meta:
        model = color
        fields = ['name',]


