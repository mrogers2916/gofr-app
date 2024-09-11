# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, QueryDict
from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializer import ServiceSerializer
from app.serializer import StoreSerializer

from app.models import Customer
from app.models import ZipCode
from app.models import Product
from app.models import Transaction
from app.models import Servicer
from app.models import Plan
from app.models import Store
from app.models import Product
from app.models import Service

from app.forms import TransactionForm
from app.forms import ServicerForm
from app.forms import PlanForm
from app.forms import StoreForm
from app.forms import ProductForm
from app.forms import CustomerForm
from app.utils import set_pagination


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

class TransactionView(View):
    context = {'segment': 'transactions'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('transactions')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('transactions')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        transactions = Transaction.objects.filter(filter_params) if filter_params else Transaction.objects.all()

        self.context['transactions'], self.context['info'] = set_pagination(request, transactions)
        if not self.context['transactions']:
            return False, self.context['info']

        return self.context, 'app/transactions/list.html'

    def edit(self, request, pk):
        transaction = self.get_object(pk)

        self.context['transaction'] = transaction
        self.context['form'] = TransactionForm(instance=transaction)

        return self.context, 'app/transactions/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        transaction = self.get_object(pk)
        form = TransactionForm(instance=transaction)
        context = {'instance': transaction, 'form': form}
        return render_to_string('app/transactions/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        transaction = get_object_or_404(Transaction, id=pk)
        return transaction

    def get_row_item(self, pk):
        transaction = self.get_object(pk)
        edit_row = render_to_string('app/transactions/edit_row.html', {'instance': transaction})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        transaction = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = TransactionForm(form_data, instance=transaction)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Transaction saved successfully')

            return True, 'Transaction saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class ServicerView(View):
    context = {'segment': 'servicers'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('servicers')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('servicers')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        servicers = Servicer.objects.filter(filter_params) if filter_params else Servicer.objects.all()

        self.context['servicers'], self.context['info'] = set_pagination(request, servicers)
        if not self.context['servicers']:
            return False, self.context['info']

        return self.context, 'app/servicers/list.html'

    def edit(self, request, pk):
        servicer = self.get_object(pk)

        self.context['servicer'] = servicer
        self.context['form'] = ServicerForm(instance=servicer)

        return self.context, 'app/servicers/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        servicer = self.get_object(pk)
        form = ServicerForm(instance=servicer)
        context = {'instance': servicer, 'form': form}
        return render_to_string('app/servicers/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        servicer = get_object_or_404(Servicer, id=pk)
        return servicer

    def get_row_item(self, pk):
        servicer = self.get_object(pk)
        edit_row = render_to_string('app/servicers/edit_row.html', {'instance': servicer})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        servicer = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = ServicerForm(form_data, instance=servicer)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Servicer saved successfully')

            return True, 'Servicer saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class PlanView(View):
    context = {'segment': 'plans'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('plans')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('plans')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        plans = Plan.objects.filter(filter_params) if filter_params else Plan.objects.all()

        self.context['plans'], self.context['info'] = set_pagination(request, plans)
        if not self.context['plans']:
            return False, self.context['info']

        return self.context, 'app/plans/list.html'

    def edit(self, request, pk):
        plan = self.get_object(pk)

        self.context['plan'] = plan
        self.context['form'] =PlanForm(instance=plan)

        return self.context, 'app/plans/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        plan = self.get_object(pk)
        form = PlanForm(instance=plan)
        context = {'instance': plan, 'form': form}
        return render_to_string('app/plans/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        plan = get_object_or_404(Plan, id=pk)
        return plan

    def get_row_item(self, pk):
        plan = self.get_object(pk)
        edit_row = render_to_string('app/plans/edit_row.html', {'instance': plan})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        plan = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = PlanForm(form_data, instance=plan)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Plan saved successfully')

            return True, 'Plan saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class StoreView(View):
    context = {'segment': 'stores'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('stores')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('plans')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        stores = Store.objects.filter(filter_params) if filter_params else Store.objects.all()

        self.context['stores'], self.context['info'] = set_pagination(request, stores)
        if not self.context['stores']:
            return False, self.context['info']

        return self.context, 'app/stores/list.html'

    def edit(self, request, pk):
        store = self.get_object(pk)

        self.context['store'] = store
        self.context['form'] =StoreForm(instance=store)

        return self.context, 'app/stores/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        store = self.get_object(pk)
        form = StoreForm(instance=store)
        context = {'instance': store, 'form': form}
        return render_to_string('app/stores/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        store = get_object_or_404(Store, id=pk)
        return store

    def get_row_item(self, pk):
        store = self.get_object(pk)
        edit_row = render_to_string('app/stores/edit_row.html', {'instance': store})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        store = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = StoreForm(form_data, instance=store)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Store saved successfully')

            return True, 'Store saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class ProductView(View):
    context = {'segment': 'products'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('products')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('products')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        products = Product.objects.filter(filter_params) if filter_params else Product.objects.all()

        self.context['products'], self.context['info'] = set_pagination(request, products)
        if not self.context['products']:
            return False, self.context['info']

        return self.context, 'app/products/list.html'

    def edit(self, request, pk):
        product = self.get_object(pk)

        self.context['product'] = product
        self.context['form'] =ProductForm(instance=product)

        return self.context, 'app/products/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        product = self.get_object(pk)
        form = ProductForm(instance=product)
        context = {'instance': product, 'form': form}
        return render_to_string('app/products/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        product = get_object_or_404(Product, id=pk)
        return product

    def get_row_item(self, pk):
        product = self.get_object(pk)
        edit_row = render_to_string('app/products/edit_row.html', {'instance': product})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        product = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = ProductForm(form_data, instance=product)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Product saved successfully')

            return True, 'Product saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class CustomerView(View):
    context = {'segment': 'customers'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('customers')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        transaction = self.get_object(pk)
        transaction.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('customers')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        customers = Customer.objects.filter(filter_params) if filter_params else Customer.objects.all()

        self.context['customers'], self.context['info'] = set_pagination(request, customers)
        if not self.context['customers']:
            return False, self.context['info']

        return self.context, 'app/customers/list.html'

    def edit(self, request, pk):
        customer = self.get_object(pk)

        self.context['customers'] = customer
        self.context['form'] = CustomerForm(instance=customer)

        return self.context, 'app/customers/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        customer = self.get_object(pk)
        form = CustomerForm(instance=customer)
        context = {'instance': customer, 'form': form}
        return render_to_string('app/customers/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        customer = get_object_or_404(Customer, id=pk)
        return customer

    def get_row_item(self, pk):
        customer = self.get_object(pk)
        edit_row = render_to_string('app/customers/edit_row.html', {'instance': customer})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        customer = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = CustomerForm(form_data, instance=customer)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'Customer saved successfully')

            return True, 'Customer saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'

class ServiceView(View):
    context = {'segment': 'services'}

    def get(self, request, pk=None, action=None):
        
        context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    # def post(self, request, pk=None, action=None):
        # self.update_instance(request, pk)
        # return redirect('services')

    # def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    # def delete(self, request, pk, action=None):
    #     transaction = self.get_object(pk)
    #     transaction.delete()

    #     redirect_url = None
    #     if action == 'single':
    #         messages.success(request, 'Item deleted successfully')
    #         redirect_url = reverse('customers')

    #     response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
    #     return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        services = Service.objects.filter(filter_params) if filter_params else Service.objects.all()

        self.context['services'], self.context['info'] = set_pagination(request, services)
        if not self.context['services']:
            return False, self.context['info']

        return self.context, 'app/services/list.html'

    # def edit(self, request, pk):
    #     customer = self.get_object(pk)

    #     self.context['customers'] = customer
    #     self.context['form'] = CustomerForm(instance=customer)

    #     return self.context, 'app/customers/edit.html'

    # """ Get Ajax pages """

    # def edit_row(self, pk):
    #     customer = self.get_object(pk)
    #     form = CustomerForm(instance=customer)
    #     context = {'instance': customer, 'form': form}
    #     return render_to_string('app/customers/edit_row.html', context)

    """ Common methods """

    # def get_object(self, pk):
    #     customer = get_object_or_404(Customer, id=pk)
    #     return customer

    # def get_row_item(self, pk):
    #     customer = self.get_object(pk)
    #     edit_row = render_to_string('app/customers/edit_row.html', {'instance': customer})
    #     return edit_row

    # def update_instance(self, request, pk, is_urlencode=False):
    #     customer = self.get_object(pk)
    #     form_data = QueryDict(request.body) if is_urlencode else request.POST
    #     form = CustomerForm(form_data, instance=customer)
    #     if form.is_valid():
    #         form.save()
    #         if not is_urlencode:
    #             messages.success(request, 'Customer saved successfully')

    #         return True, 'Customer saved successfully'

    #     if not is_urlencode:
    #         messages.warning(request, 'Error Occurred. Please try again.')
    #     return False, 'Error Occurred. Please try again.'


# API Views
class ServiceApiView(APIView):
    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckZipCodeView(APIView):
    def get(self, request, zip_code):
        exists = ZipCode.objects.filter(code=zip_code).exists()
        return Response({'zip_code_exists': exists}, status=status.HTTP_200_OK)

class StoreProductCheckView(APIView):
    def post(self, request):
        # Deserialize the incoming data
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            store_data = serializer.validated_data
            product_data = store_data.pop('product')
            
            # Check if the product exists and is serviceable
            product_exists = Product.objects.filter(
                name=product_data['name'],
                category=product_data['category'],
                subcategory=product_data['subcategory'],
                serviceable=product_data['serviceable']
            ).exists()
            
            if not product_exists:
                return Response({"message": "Product does not exist or is not serviceable"}, status=status.HTTP_404_NOT_FOUND)
            
            # Check if the store exists with the given product
            store_exists = Store.objects.filter(
                store_name=store_data['store_name'],
                rev_share=store_data['rev_share'],
                ecommerce_platform=store_data['ecommerce_platform'],
                product__name=product_data['name'],  # Ensure the store has the given product
                product__category=product_data['category'],
                product__subcategory=product_data['subcategory'],
                product__serviceable=product_data['serviceable']
            ).exists()
            
            if store_exists:
                return Response({"message": "Store and product exist"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Store does not exist or does not have the specified product"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)