from django import forms
from .models import *

# Django Forms API
# Django REST framework: django-rest-framework.org

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'description', 'category',)