# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

    
class Servicer(models.Model):
    name = models.CharField(max_length=100)
    service_cost = models.CharField(max_length=100)
    rev_share = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'servicers'
        verbose_name_plural = 'servicers'

class ZipCode(models.Model):
    zip_code = models.CharField(max_length=5)
    servicer = models.ForeignKey(Servicer, related_name='zip_code', on_delete=models.CASCADE)

class Plan(models.Model):
    consumer_facing_price = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=100)

    def __str__(self):
        return self.plan_type

    class Meta:
        verbose_name = 'plans'
        verbose_name_plural = 'plans'

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    rev_share = models.CharField(max_length=100)
    ecommerce_platform = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name = 'stores'
        verbose_name_plural = 'stores'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    serviceable = models.BooleanField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=5)
    delivery_date = models.DateField()
    service_date = models.DateField()
    service_time = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'customers'
        verbose_name_plural = 'customers'

class Service(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    servicer = models.ForeignKey(Servicer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'services'
        verbose_name_plural = 'services'

class Transaction(models.Model):
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    @property
    def status_info(self):
        res = {'class': None}

        if self.status == "Paid":
            res['class'] = 'text-success'
        elif self.status == "Due":
            res['class'] = 'text-warning'
        elif self.status == "Canceled":
            res['class'] = 'text-danger'

        return res