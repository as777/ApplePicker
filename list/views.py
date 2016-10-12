from django.shortcuts import render

# Create your views here.
from django.http import HTTPResponse

def listing(request):
    items = list.objects.all()
    return render(request, "all_itmes.html", {'items': items})
