import imp
import json
from django.http.response import JsonResponse
from django.shortcuts import render
from DigitalBazzar.forms import Update_profile
from .models import  Products,Cart,Order,Shipping
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.messages import success



def  Product_View(request):
    products=Products.objects.all()
    template="DigitalBazzar/products.html"
    if request.user.is_authenticated:
        order,created=Order.objects.get_or_create(customer=request.user.customer,status=False)
        context_object_name={'products':products,'order':order}
        if request.method=="GET":
            search=request.GET.get('search')
            if search!=None:
                context_object_name['products']=Products.objects.filter(name__icontains=search)
                context_object_name['search']=search
        return render(request,template,context_object_name)
    context_object_name={'products':products}
    if request.method=="GET":
        search=request.GET.get('search')
        context_object_name['products']=Products.objects.filter(name__icontains=search)
        context_object_name['search']=search

    return render(request,template,context_object_name)
@login_required(login_url='login')
def profile(request):
    template_name="DigitalBazzar/profile.html"
    form=Update_profile(instance=request.user.customer)
    if request.method=='POST':
        form=Update_profile(request.POST,request.FILES,instance=request.user.customer)
        if form.is_valid():
            form.save()
            success(request,'profile updated successfully..')
    context_object_name={'form':form}
    return render(request,template_name,context_object_name)


@login_required(login_url="login")
def Dash_board(request):
    order, created=Order.objects.get_or_create(customer=request.user.customer,status=False)
    all_order=Order.objects.filter(customer=request.user.customer)
    place_order=Order.objects.filter(status=True,customer=request.user.customer)
    carts=order.cart_set.all()
    context_object_name={'carts':carts,'order':order,'all_order':all_order,'place_orders':place_order}     
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
def shipping(request):
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
    print(order)

    # name=form['form']['name']
    email=form['form']['email']
    address=form['form']['address']
    state=form['form']['state']
    zips=form['form']['zip']
    city=form['form']['city']
    phone=form['form']['phone']
    total=form['form']['total']

 
    if(int(total)==order.get_total):
        order.status=True
        order.save()
    else:
        print("not equal")
    print(order.status)
    if order.status==True:
        Shipping.objects.create(
        customer=request.user.customer,
        order=order,
        address=address,
        code=zips,
        phone=phone,
        email=email,
        city=city,
        state=state
        )
        print("shipping  created")

        return JsonResponse('successed',safe=False)
   
    else:
        return JsonResponse('Unsuccessedful',safe=False)


 


    
