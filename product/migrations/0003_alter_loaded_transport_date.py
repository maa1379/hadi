# Generated by Django 3.2.1 on 2022-02-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220215_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaded',
            name='transport_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
