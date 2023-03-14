from django.shortcuts import HttpResponse,render, redirect
from . models import Category, Item
# from . forms import CreateAbcForm

import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)

def index(request):
    return render(request, 'index.html')


def table(request, id):
    rows = Item.objects.filter(category_id__gt=id)
    print("id: ", id)
    print(rows.values_list())
    context = {'rows': rows.values_list()}
    return render(request, 'table.html', context)

def category(request):
    # from orm_store_app.models import Category, Item
    objects = Category.objects.all().values()
    print("objects:\n", list(objects))
    context={'objects_list': list(objects)}
    return render(request, 'category.html', context)

def page(request, id):
    # from orm_store_app.models import  Category, Item
    category = Category.objects.values()
    print("category:\n", category)
    category_context = {'category': category}

    items = Item.objects.values().filter(category=id)
    print("items:\n", items)
    for i in items:
        lst= list((i['image'].split('/'))[-2:])
        img_value = (lst[0] + '/' + lst[1])
        print (img_value)
        i['image'] = img_value
    items_context = {'items': items}
    context = {"category_context": category_context, "items_context": items_context  }
    return render(request, 'page.html', context)
