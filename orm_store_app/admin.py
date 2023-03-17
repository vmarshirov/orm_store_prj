from django.contrib import admin
from .models import  Category, Item

admin.site.register(Category)
admin.site.register(Item)

# Register your models here.
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     pass
#     list_display = ['id', 'category', 'name',  'price']
#     list_editable = ['name', 'category']
#     search_fields = ['name']
#     list_filter = ['name', 'price']
#     list_per_page = 15
