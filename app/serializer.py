from rest_framework import serializers
from .models import Customer, Product, Service, Store, Plan, Servicer, Transaction, ZipCode


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'rev_share', 'ecommerce_platform']  # Include other fields as needed

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'consumer_facing_price', 'plan_type']  # Include other fields as needed


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    plan = PlanSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'serviceable',
                  'store', 'plan']  # Include other fields as needed

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'address',
                  'delivery_date', 'service_date', 'service_time']

class ServicerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'service_cost', 'rev_share']

class ServiceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    servicer = ServicerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Service
        fields = ['customer', 'servicer', 'product']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        servicer_data = validated_data.pop('servicer')
        product_data = validated_data.pop('product')
        store_data = product_data.pop('store')
        plan_data = product_data.pop('plan')

        store, _ = Store.objects.get_or_create(**store_data)
        plan, _ = Plan.objects.get_or_create(**plan_data)
        customer, _ = Customer.objects.get_or_create(**customer_data)
        servicer, _ = Servicer.objects.get_or_create(**servicer_data)
        product, _ = Product.objects.get_or_create(store=store, plan=plan, **product_data)

        service = Service.objects.create(customer=customer, servicer=servicer, product=product, **validated_data)

        # Create a Transaction entry
        transaction_data = {
            'total_cost': 98.00,  # Set this value dynamically based on your business logic
            'due_date': customer.service_date,
            'status': "Due",
            'description': f"Transaction for {service.customer.first_name} - {service.servicer.name}"
        }

        Transaction.objects.create(**transaction_data)
        
        return service
