from django.shortcuts import render
from .models import ShippingAddress
# Create your views here.

def payment_success(request):

    # user without accounts. empty form
    return render(request,'payment/payment-success.html')



def payment_failed(request):

    return render(request,'payment/payment-failed.html')

def checkout(request):
     # user with accounts. pre filled details
    if request.user.is_authenticated:

        try:

            # authnticated user with shipping address
            shipping_address=ShippingAddress.objects.get(user=request.user)

            context={'shipping':shipping_address}

            return render(request,'payment/checkout.html',context=context)
        

        except ShippingAddress.DoesNotExist:

            # authenticated user without shipping address
            return render(request,'payment/checkout.html')
        
        
    return render(request,'payment/checkout.html')