# Generated by Django 4.1.7 on 2023-04-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_store_app', '0012_alter_item_category_alter_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='vendor_code',
            field=models.IntegerField(default=0, verbose_name='Артикул'),
        ),
    ]
