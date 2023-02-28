from django.contrib import admin
from django.urls import path
from .views.Home import index
from  .views.SignIn import SignIn
from  .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import checkout
from  .views.orders import orderview
from .middlewares.auth import auth_middleware
#from .views import Home, login , SignIn


urlpatterns = [
    path('', index.as_view() , name='homepage'),
    path('SignIn', SignIn.as_view(), name = 'signin' ),
    path('login' ,Login.as_view(), name ='login' ),
    path('logout' , logout, name ='logout' ),
path('cart' , Cart.as_view(), name ='cart' ),
path('check-out' , checkout.as_view(), name ='checkout' ),
#path('Orders', auth_middleware(order.as_view()), name ='orders')
path('Orders', orderview.as_view(), name ='orders')
]
