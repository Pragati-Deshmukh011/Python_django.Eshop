from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.Product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class orderview(View):

    def get(self, request):

        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        #orders = orders.reverse()
        return render(request, 'orders.html', {'orders': orders})

