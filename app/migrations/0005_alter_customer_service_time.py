# Generated by Django 4.2 on 2024-04-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_serviceeable_product_serviceable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='service_time',
            field=models.TimeField(),
        ),
    ]
