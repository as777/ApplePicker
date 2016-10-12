from django import forms

# Django Forms API
# Django REST framework: django-rest-framework.org

class ItemForm(forms.Form):
    name = forms.CharField(label="Item Name", max_length=50)
    description = forms.CharField(label="Item Description")