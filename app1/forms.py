from django import forms
from .models import *

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description']

class InventoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description']


class AddInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'type', 'color', 'price', 'description']