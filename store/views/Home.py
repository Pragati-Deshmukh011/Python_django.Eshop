from django.shortcuts import render, redirect
from store.models.Product import Products
from store.models.category import Category
from django.views import View

# Create your views here.
class index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                      cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        Product = None
        # Product = Products.get_all_products();
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        print(request.GET)
        if categoryId:
            Product = Products.get_all_products_by_categoryid(categoryId)
        else:
            Product = Products.get_all_products();
        data = {}
        data['products'] = Product
        data['categories'] = categories
        print('You are: ', request.session.get('email'))
        return render(request, 'index.html', data)



