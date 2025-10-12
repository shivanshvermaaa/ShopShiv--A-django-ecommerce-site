from django.db import models
from django.contrib.auth.models import User

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
        return 'shipping address -'+self.id

    class Meta:
        verbose_name_plural='Shipping Addresses'