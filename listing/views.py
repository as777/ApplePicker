from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

# Django docs: topics/http/views/

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *

def index(request):
    return render(request, "listing/index.html")

class ListingView(generic.ListView):
    template_name = 'listing/all_items.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Item
    template_name = 'listing/detail.html'

def item_edit(request, pk):
    i = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=i)
        if form.is_valid():
            i = form.save(commit=False)
            i.save()
            return redirect('item_detail', pk=i.id)
    else:
        form = ItemForm(instance=i)

    return render(request, "listing/item_edit.html", {"form": form})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.date_entry = timezone.now()
            new_item.save()
            return redirect('item_detail', pk=new_item.id)
    else:
        form = ItemForm()

    return render(request, 'listing/item_new.html', {'form': form})

class DeleteView(generic.edit.DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')

    template_name = 'listing/item_delete.html'
