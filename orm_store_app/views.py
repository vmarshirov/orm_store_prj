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
    print("pk: ", pk)
    objects_list = Item.objects.filter(category_id__gt=pk).values().order_by('-category_id')
    print('objects_list: ', objects_list)
    context = {'objects_list': objects_list}
    return render(request, 'table.html', context)

def category(request):
    # from orm_store_app.models import Category, Item
    objects = Category.objects.all().values()
    print("objects:\n", list(objects))
    context={'objects_list': list(objects)}
    return render(request, 'category.html', context)

def page(request, pk):
    # from orm_store_app.models import  Category, Item
    category = Category.objects.values()
    print("category:\n", category)
    # category = {'category': category}

    items = Item.objects.values().filter(category=pk)
    print("\nitems:\n", items)
    for item in items:
        print('\nitem: ', item)
        lst= list((item['image'].split('/'))[-2:])
        img_value = (lst[0] + '/' + lst[1])
        print ('img_value: ', img_value)
        item['image'] = img_value
    print("items:\n", items)
    # items = {'items': items}
    context = {"category": category, "items": items  }
    return render(request, 'page.html', context)


def store_result(request):
    print(request.GET)
    return HttpResponse(f"""
    """)