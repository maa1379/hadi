# Generated by Django 3.2.1 on 2022-02-19 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220219_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linedproducts',
            name='line_number',
        ),
    ]
