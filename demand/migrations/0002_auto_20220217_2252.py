# Generated by Django 3.2.1 on 2022-02-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hold',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='field',
            field=models.CharField(blank=True, choices=[('stone_cutting_factory', 'کارخانه سنگ بری'), ('export', 'صادرات'), ('block_warehouse', 'انبار بلوک'), ('internal_sales_of_blocks', 'فروش داخلی بلوک')], max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='demand/'),
        ),
        migrations.AddField(
            model_name='hold',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='last_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='male',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='pin',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hold',
            name='tonnage',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='field',
            field=models.CharField(blank=True, choices=[('stone_cutting_factory', 'کارخانه سنگ بری'), ('export', 'صادرات'), ('block_warehouse', 'انبار بلوک'), ('internal_sales_of_blocks', 'فروش داخلی بلوک')], max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='demand/'),
        ),
        migrations.AddField(
            model_name='sample',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='last_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='male',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='pin',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='tonnage',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='company',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='field',
            field=models.CharField(blank=True, choices=[('stone_cutting_factory', 'کارخانه سنگ بری'), ('export', 'صادرات'), ('block_warehouse', 'انبار بلوک'), ('internal_sales_of_blocks', 'فروش داخلی بلوک')], max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='demand/'),
        ),
        migrations.AddField(
            model_name='visit',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='last_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='male',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='occupation',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='pin',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='tonnage',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='visit_date',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='visit_hour',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='visit_minute',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
