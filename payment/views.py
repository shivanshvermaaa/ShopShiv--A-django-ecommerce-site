from django.shortcuts import render
from .models import ShippingAddress, Order, OrderItem
from cart.cart import Cart
from django.http import JsonResponse
# Create your views here.

def payment_success(request):
    for key in list (request.session.keys()):
        if key== 'session_key':
            del request.session[key]
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

def complete_order(request):
    if request.POST.get('action') == 'post':
        
        # get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2= request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')


        shipping_address= (address1 + ' ' + address2 + ' ' 
                            + city + ' ' + state + ' ' + zipcode)
        

        cart=Cart(request)
        total_cost=cart.get_total()


        '''
        ORDER VARIATIONS :
        1- create order for -> acc users with + without shipping address
        2- create order for -> guest users

        '''

        if request.user.is_authenticated:
            order=Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost,
                user=request.user
            )

            # will be used as a fk in order item
            order_id =order.pk

            for item in cart:
                OrderItem.objects.create(
                    order_id =order_id,
                    product= item['product'],
                    quantity= item['qty'],
                    price= item['price'],
                    user= request.user
                )

        else:

            order=Order.objects.create(
                full_name=name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=total_cost
                
            )

    # will be used as a fk in order item
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(
                    order_id =order_id,
                    product= item['product'],
                    quantity= item['qty'],
                    price= item['price']
                    
                )


        order_success= True
        response= JsonResponse({'success':order_success})
        return response       


