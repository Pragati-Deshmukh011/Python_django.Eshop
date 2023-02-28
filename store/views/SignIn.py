from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class SignIn(View):
    def get(self, request):
        return render(request, 'SignIn.html')

    def post(self, request):
        postData = request.POST
        # request.POST.get('first_name')
        first_name = postData.get('Fname')
        last_name = postData.get('lname')
        password = postData.get('password')
        email = postData.get('email')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email

        }

        customer = Customer(first_name=first_name, last_name=last_name, email=email, password=password)
        error_msg = self.validateCustomer(customer)
        # saaving
        if not error_msg:
            print(first_name, last_name, password, email)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_msg,
                'values': value
            }

            return render(request, 'SignIn.html', data)

    def validateCustomer(self, customer):
        error_msg = None;
        if (not customer.first_name):
            error_msg = "First name required!!"
        elif len(customer.first_name) < 4:
            error_msg = 'First name must be greater than 4'
        elif not len(customer.last_name):
            error_msg = 'last name required!!'
        elif len(customer.last_name) < 4:
            error_msg = 'last name must be greater than 4'
        elif not len(customer.password):
            error_msg = 'Password is required'
        elif len(customer.password) < 4:
            error_msg = 'password must be greater than 8'
        elif not len(customer.email):
            error_msg = 'email is required!!'
        elif len(customer.email) < 7:
            error_msg = 'email must greater than 7'

        elif customer.isExists():
            error_msg = 'Email is already register...'
        return error_msg
