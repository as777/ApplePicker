from django import forms
from .models import Item

# Django Forms API
# Django REST framework: django-rest-framework.org

class ItemForm(forms.Form):
    name = forms.CharField(label="Item Name", max_length=50)
    description = forms.CharField(label="Description")
    category = forms.ModelChoiceField(queryset=Item, to_field_name="category")