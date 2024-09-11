from django import forms

from app.models import Transaction
from app.models import Servicer
from app.models import Plan
from app.models import Store
from app.models import Product
from app.models import Customer


class TransactionForm(forms.ModelForm):

    due_date = forms.DateField(label="Due Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    total_cost = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    class Meta:
        model = Transaction
        fields = [ 'due_date', 'total_cost', 'status']

class ServicerForm(forms.ModelForm):
    name = forms.CharField(label="Servicer Name", widget=forms.TextInput(attrs={'class': 'form-control servicer'}))
    rev_share = forms.CharField(label="Rev Share", widget=forms.TextInput(attrs={'class': 'form-control servicer'}))
    service_cost = forms.CharField(label="Service Cost", widget=forms.TextInput(attrs={'class': 'form-control servicer'}))

    class Meta:
        model = Servicer
        fields = ['name', 'rev_share', 'service_cost']

class PlanForm(forms.ModelForm):
    consumer_facing_price = forms.CharField(label="Servicer Name", widget=forms.TextInput(attrs={'class': 'form-control plan'}))
    plan_type = forms.CharField(label="Zip Code", widget=forms.TextInput(attrs={'class': 'form-control plan'}))

    class Meta:
        model = Plan
        fields = ['consumer_facing_price', 'plan_type']


class StoreForm(forms.ModelForm):
    store_name = forms.CharField(label="Store Name", widget=forms.TextInput(attrs={'class': 'form-control store'}))
    rev_share = forms.CharField(label="Rev Share %", widget=forms.TextInput(attrs={'class': 'form-control store'}))
    ecommerce_platform = forms.CharField(label="Ecommerce Platform", widget=forms.Select(attrs={'class': 'form-control store'}))

    class Meta:
        model = Store
        fields = ['store_name', 'rev_share', 'ecommerce_platform']

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control product'}))
    category = forms.CharField(label="Category", widget=forms.TextInput(attrs={'class': 'form-control product'}))
    subcategory = forms.CharField(label="Subcategory", widget=forms.TextInput(attrs={'class': 'form-control product'}))
    serviceable = forms.CharField(label="Serviceable", widget=forms.Select(attrs={'class': 'form-control product'}))
    store = forms.CharField(label="Store", widget=forms.Select(attrs={'class': 'form-control product'}))
    plan = forms.CharField(label="Plan", widget=forms.Select(attrs={'class': 'form-control product'}))

    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory', 'serviceable', 'store', 'plan']

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'form-control customer'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control customer'}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control customer'}))
    zip_code = forms.CharField(label="Zip Code", widget=forms.TextInput(attrs={'class': 'form-control customer'}))
    address = forms.CharField(label="Address", widget=forms.Select(attrs={'class': 'form-control customer'}))
    delivery_date = forms.CharField(label="Delivery Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input customer', 'placeholder': 'yyyy-mm-dd'}))
    service_date = forms.CharField(label="Service Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input customer', 'placeholder': 'yyyy-mm-dd'}))
    service_time = forms.CharField(label="Service Time", widget=forms.TimeInput(attrs={'class': 'form-control customer'}))

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'address', 'delivery_date', 'service_date', 'service_time']
