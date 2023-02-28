# Generated by Django 4.1.7 on 2023-02-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_store_app', '0003_alter_category_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Названия'},
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
