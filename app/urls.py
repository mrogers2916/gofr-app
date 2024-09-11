# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import CheckZipCodeView, CheckProductView, StoreProductCheckView, ServiceApiView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(), name='transactions'),

    re_path(r'^servicers/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.ServicerView.as_view(), name='servicers'),
    re_path(r'^plans/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.PlanView.as_view(), name='plans'),
    re_path(r'^stores/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.StoreView.as_view(), name='stores'),
    re_path(r'^products/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.ProductView.as_view(), name='products'),
    re_path(r'^customers/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.CustomerView.as_view(), name='customers'),
    re_path(r'^services/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.ServiceView.as_view(), name='services'),

    path('api/check-zipcode/<str:zip_code>/', CheckZipCodeView.as_view(), name='check-zipcode'),
    path('api/store-product/check/', StoreProductCheckView.as_view(), name='store-product-check'),
    path('api/service', ServiceApiView.as_view(), name='service'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
