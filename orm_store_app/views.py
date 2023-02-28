from django.shortcuts import HttpResponse,render, redirect
from . models import Category, Item
# from . forms import CreateAbcForm

import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)

def index(request):
    return render(request, 'index.html')


def table(request, pk):
    rows = Item.objects.filter(category_id__gt=pk)
    print("pk: ", pk)
    print(rows.values_list())
    context = {'rows': rows.values_list()}
    return render(request, 'table.html', context)

def category(request):
    # from orm_store_app.models import Category, Item
    objects = Category.objects.all().values()
    print("objects:\n", list(objects))
    context={'objects_list': list(objects)}
    return render(request, 'category.html', context)

def page(request, pk):
    # from orm_store_app.models import  Category, Item
    objects = Category.objects.all().values()
    print("objects:\n", list(objects))
    context_0={'objects_list': list(objects)}

    rows = Item.objects.filter(category=pk)
    print("rows:\n", list(rows.values_list()))
    context_1 = {'rows': list(rows.values_list())}
    context = {"context_0": context_0, "context_1": context_1  }
    return render(request, 'page.html', context)