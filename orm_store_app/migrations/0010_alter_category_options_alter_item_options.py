# Generated by Django 4.1.7 on 2023-03-22 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_store_app', '0009_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
