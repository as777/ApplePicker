from django.contrib import admin
from listing.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'is_done', 'date_entry')
    list_editable = ('is_done', 'description')

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Item, ItemAdmin)
# admin.site.register(Category, CategoryAdmin)


