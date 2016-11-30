from django.contrib import admin
from listing.models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'is_done', 'date_entry')
    list_editable = ('is_done', 'description')

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'origin', 'date_entry')

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Quote, QuoteAdmin)
# admin.site.register(Category, CategoryAdmin)


