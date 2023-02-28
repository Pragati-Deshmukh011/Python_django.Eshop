from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.Product import Products
from store.models.orders import Order

class checkout(View):
    def post(self, request):
       address = request.POST.get('Address')
       phone = request.POST.get('Phone-number')
       customer = request.session.get('customer')
       cart = request.session.get('cart')
       #Date = request.session.get('Date')
       products = Products.get_products_by_id(list(cart.keys()))
       print(address, phone ,customer, cart, products)

       for products in products:
          print(cart.get(str(products.id)))
          order = Order(customer = Customer(id = customer), product = products,
                        price = products.price, quantity =cart.get(str(products.id)),
                        address =address, phone = phone)
          print(order.place_order());
          # order.save()
          request.session['cart'] ={}
       return redirect('cart')

