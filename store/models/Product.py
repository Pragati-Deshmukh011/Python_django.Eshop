from django.db import models
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete= models.CASCADE ,default=1)
    description =models.CharField(max_length=300,default='')
    image=models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in= ids)


    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(Category_id):
        if Category_id:
           return Products.objects.filter(category = Category_id)
        else:
           return Products.get_all_products();