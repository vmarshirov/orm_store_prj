# Generated by Django 4.1.7 on 2023-03-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_store_app', '0007_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='orm_store_app/static/item_images'),
        ),
    ]