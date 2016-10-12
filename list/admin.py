from django.contrib import admin
from list.models import Item, Category

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'date_entry', 'is_done')
    list_editable = ("is_done",)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)


