# import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='Категория',  on_delete=models.CASCADE)
    name = models.CharField('Товар', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.FloatField('Цена', )
    vendor_code = models.IntegerField('Артикул',  blank=False , null=False)
    image = models.ImageField(upload_to='orm_store_app/static/item_images', blank=True, null=True)
    is_sold = models.BooleanField('Проданы', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self):
        return '%s %s' % (self.category, self.name)
        # return self.name

# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)


# python manage.py makemigrations
# python manage.py migrate


# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']


# c_choices = (
#     (0, "ноль"),
#     (10, "десять"),
#     (15, "пятнадцать"),
#     (20, "двадцать"),
# )
#
#
# class Store(models.Model):
#     task = models.CharField("Формулировка задачи", default="Равна ли С сумме A и B ?", max_length=256)
#     a = models.IntegerField("Значение А", default=0, )
#     b = models.IntegerField("Значение B", default=0, help_text="Подсказка для поля")
#     c = models.IntegerField("Значение С", choices=c_choices, default=0, )
#     current_date = models.DateTimeField("Дата Записи", auto_now=True)
#
#     def __str__(self):
#         # return self.task
#         return '%s %s' % (self.task, self.current_date)
#
#     class Meta:
#         verbose_name = "A_B_C"
#         verbose_name_plural = "A_B_C_S"
#         # ordering = ("-c", "b")
