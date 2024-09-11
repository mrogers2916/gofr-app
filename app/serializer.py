from rest_framework import serializers
from .models import Customer, Product, Service, Store, Plan, Servicer, Transaction, ZipCode

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'consumer_facing_price', 'plan_type']  # Include other fields as needed


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'serviceable']  # Include other fields as needed

class StoreSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Store has a product
    plan = PlanSerializer()  # Store has a plan
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'rev_share', 'ecommerce_platform', 'product', 'plan']  # Include other fields as needed

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
    store = StoreSerializer()

    class Meta:
        model = Service
        fields = ['customer', 'servicer', 'store']

    def create(self, validated_data):
        # Handle Customer creation or lookup
        customer_data = validated_data.pop('customer')
        customer, _ = Customer.objects.get_or_create(**customer_data)

        # Handle Servicer creation or lookup
        servicer_data = validated_data.pop('servicer')
        servicer, _ = Servicer.objects.get_or_create(**servicer_data)

        # Handle Product and Store creation or lookup
        store_data = validated_data.pop('store')
        product_data = store_data.pop('product')
        plan_data = store_data.pop('plan')
        
        product, _ = Product.objects.get_or_create(**product_data)
        plan, _ = Plan.objects.get_or_create(**plan_data)
        store, _ = Store.objects.get_or_create(product=product, plan=plan, **store_data)

        # Create the Service entry
        service = Service.objects.create(customer=customer, servicer=servicer, store=store)
        # Create a Transaction entry
        transaction_data = {
            'total_cost': 98.00,  # Set this value dynamically based on your business logic
            'due_date': customer.service_date,
            'status': "Due",
            'description': f"Transaction for {service.customer.first_name} - {service.servicer.name}"
        }

        Transaction.objects.create(**transaction_data)
        
        return service
