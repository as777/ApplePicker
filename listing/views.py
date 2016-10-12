from django.shortcuts import render

# Django docs: topics/http/views/

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item
from .forms import ItemForm

def listing(request):
    items = Item.objects.all()
    return render(request, "listing/all_items.html", {'items_list': items})

def detail(request, item_id):
    try:
        i = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    return render(request, "listing/detail.html", {'item': i})

def item_edit(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("listing/all_items")

    else:
        form = ItemForm()

    return render(request, "listing/item_edit.html", {"form": form})