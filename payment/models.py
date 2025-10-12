from django.db import models
from django.contrib.auth.models import User
from store.models import Product


# Create your models here.

class ShippingAddress(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    # foreign key, relation with user
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=100)

    # optional fields
    state=models.CharField(max_length=100,null=True,blank=True)
    zipcode=models.CharField(max_length=20,null=True,blank=True)
    country=models.CharField(max_length=100)
    
    def __str__(self):
        return 'shipping address -'+ str(self.id)

    class Meta:
        verbose_name_plural='Shipping Addresses'



class Order(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    shipping_address=models.CharField(max_length=200)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return 'order - #' + str(self.id)

    class Meta:
        verbose_name_plural='Orders'


class OrderItem(models.Model):
    quantity=models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null= True,blank= True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return 'order item - #' + str(self.id)
    
    class Meta:
        verbose_name_plural='Order Items'