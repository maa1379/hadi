# Generated by Django 3.2.1 on 2022-02-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_loaded_transport_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaded',
            name='transport_date',
            field=models.DateField(),
        ),
    ]
