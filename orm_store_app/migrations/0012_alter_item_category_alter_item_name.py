# Generated by Django 4.1.7 on 2023-03-22 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_store_app', '0011_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Категория', to='orm_store_app.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Товар'),
        ),
    ]
