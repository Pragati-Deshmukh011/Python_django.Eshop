import datetime
from django.db import models
from .Product import Products
from .customer import Customer
class Order(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200,default='', blank=True)
    phone = models.CharField(max_length=10,default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    Status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):

        return Order.objects.filter(customer = customer_id).order_by('-date')
