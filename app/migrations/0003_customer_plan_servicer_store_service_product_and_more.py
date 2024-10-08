# Generated by Django 4.2 on 2024-04-24 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('delivery_date', models.DateField()),
                ('service_date', models.DateField()),
                ('service_time', models.DateField()),
            ],
            options={
                'verbose_name': 'customers',
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_facing_price', models.CharField(max_length=100)),
                ('plan_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'plans',
                'verbose_name_plural': 'plans',
            },
        ),
        migrations.CreateModel(
            name='Servicer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('service_cost', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'servicers',
                'verbose_name_plural': 'servicers',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('rev_share', models.CharField(max_length=100)),
                ('ecommerce_platform', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'stores',
                'verbose_name_plural': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('servicer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicer')),
            ],
            options={
                'verbose_name': 'services',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
                ('serviceeable', models.BooleanField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.plan')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.store')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='servicer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
