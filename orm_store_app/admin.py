from django.contrib import admin
from .models import  Category, Item

# Register your models here.
# @admin.register(Store)
# class StoreAdmin(admin.ModelAdmin):
#     pass
#     list_display = ['pk', 'task', 'a', 'b', 'c', 'current_date']
#     list_editable = ['task', 'a', 'b', 'c']
#     search_fields = ['task', 'a', 'b', 'c']
#     list_filter = ['task', 'a', 'b', 'c']
#     list_per_page = 5

admin.site.register(Category)
admin.site.register(Item)
