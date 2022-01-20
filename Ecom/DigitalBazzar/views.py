import imp
import json
import xml
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import  Customer, Products,Cart,Order
from django.contrib.auth.decorators import login_required
import datetime


def  Product_View(request):
    products=Products.objects.all()
    template="DigitalBazzar/products.html"
    if request.user.is_authenticated:
        order,created=Order.objects.get_or_create(customer=request.user.customer,status=False)
        context_object_name={'products':products,'order':order}
        return render(request,template,context_object_name)
    
    context_object_name={'products':products}

    return render(request,template,context_object_name)


@login_required(login_url="login")
def Dash_board(request):
    order, created=Order.objects.get_or_create(customer=request.user.customer,status=False)
    carts=order.cart_set.all()
    context_object_name={'carts':carts,'order':order}     
    template="DigitalBazzar/dashboard.html"

    return render(request,template,context_object_name)

@login_required(login_url="login")
def Carts(request):
    customer=request.user.customer
    order, created =Order.objects.get_or_create(customer=customer,status=False)
    items= order.cart_set.all()
    context_object_name={'items':items,'order':order}   
    
    return render(request,"DigitalBazzar/cart.html",context_object_name)


@login_required(login_url="login")
def update_cart(request):
    data = json.loads(request.body) 
    customer=request.user.customer
   
    pro_id=int(data['productId'])
    action=data['action']

    product=Products.objects.get(id=int(pro_id))
    order, created = Order.objects.get_or_create(customer=customer,status=False)
    cart, created= Cart.objects.get_or_create(order=order , product=product)

    if action=="add":
        print(cart.quantity)
        cart.quantity=(cart.quantity+1)
    elif action=="remove":
        cart.quantity=(cart.quantity-1)
    cart.save()

    if cart.quantity<=0:
        cart.delete()

    return JsonResponse("cart updated",safe=False)

@login_required(login_url="login")
def Shipping(request):
    order=Order.objects.get(customer=request.user.customer,status=False)
    items= order.cart_set.all()
    context_object_name={'items':items,'order':order}
    template="DigitalBazzar/shipping.html"

    return render(request,template,context_object_name)
    

@login_required(login_url="login")
def Processing(request):
    form=json.loads(request.body)
    transaction_id=datetime.datetime.now().timestamp()

    order, created=Order.objects.get_or_create(customer=request.user.customer,status=False)
    order.transaction_id=transaction_id

    name=form['form']['name']
    email=form['form']['email']
    address=form['form']['address']
    state=form['form']['state']
    zip=form['form']['name']
    city=form['form']['email']
    phone=form['form']['name']
    total=form['form']['total']
    print(total)
    print(order.get_total)

    if(total==order.get_total):
        order.status==True
        order.save()

    if order.status==True:

        Shipping.objects.create(

        customer=name,
        order=order,
        address=address,
        code=zip,
        phone=phone,
        email=email,
        city=city,
        state=state
        )
        Shipping.save()
        return JsonResponse('successed',safe=False)
   
    else:
        return JsonResponse('Unsuccessedful',safe=False)


 


    
