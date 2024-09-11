# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from app.models import Transaction
from app.models import Servicer
from app.models import Plan
from app.models import Store
from app.models import Product
from app.models import Customer
from app.models import Service
from import_export import resources
from import_export.admin import ImportMixin


class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ['id', 'issue_date', 'due_date', 'total_cost', 'description', 'status', 'created_time', 'updated_time']
@admin.register(Transaction)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'issue_date', 'due_date', 'total_cost', 'description', 'status', 'created_time', 'updated_time']
    resource_class = TransactionResource


class ServicerResource(resources.ModelResource):
    class Meta:
        model = Servicer
        fields = ['id', 'name', 'zip_code', 'service_cost']

@admin.register(Servicer)
class ServicerAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'zip_code', 'service_cost']
    resource_class = ServicerResource


class PlanResource(resources.ModelResource):
    class Meta:
        model = Plan
        fields = ['id', 'consumer_facing_price', 'plan_type']

@admin.register(Plan)
class PlanAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'consumer_facing_price', 'plan_type']
    resource_class = PlanResource


class StoreResource(resources.ModelResource):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'rev_share', 'ecommerce_platform']

@admin.register(Store)
class StoreAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'store_name', 'rev_share', 'ecommerce_platform']
    resource_class = StoreResource


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'serviceable', 'store', 'plan']

@admin.register(Product)
class ProductAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'subcategory', 'serviceable', 'store', 'plan']
    resource_class = ProductResource


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'email', 'address', 'delivery_date',
                  'service_date', 'service_time']

@admin.register(Customer)
class CustomerAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'delivery_date', 'service_date', 'service_time']
    resource_class = CustomerResource


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = ['id', 'customer', 'servicer']

@admin.register(Service)
class ServiceAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'customer', 'servicer']
    resource_class = ServiceResource

