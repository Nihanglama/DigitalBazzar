import imp
from django.db import models
from django.contrib.auth.models  import User
from django.db.models.signals import post_save



class Products(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)
    picture=models.ImageField(default="books.jpg",null=True,blank=True)
    given_cat=(
    ('cloths','cloths'),
    ('food','food'),        
    ('shoes','shoes'),
    ('iots','iots'),
    ('books','books'),
    ('sports','sports'),
    )
    category=models.CharField(max_length=200,null=True,choices=given_cat)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name


class Customer(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=False)
    address=models.CharField(max_length=300,null=True,blank=True)
    email=models.CharField(max_length=300,null= True,blank=True)
    picture=models.ImageField(default='fb.jpeg')

    def __str__(self):
        return  self.name

def create(sender,instance,created,*args, **kwargs):
    if created:
        Customer.objects.create(user=instance,name=instance.username)

post_save.connect(create,sender=User)



class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True,blank=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total(self):
        orderitem=self.cart_set.all()
        total=sum([item.get_item_sum for item in orderitem])

        return total
    
    @property
    def total_item(self):
        items=self.cart_set.all()
        total=sum([item.quantity for item in items])

        return total



class Cart(models.Model):
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,null=True,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,null=True,blank=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    @property
    def get_item_sum(self):
        self.total=self.product.price * self.quantity
        return self.total

class Shipping(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=False,null=True)
    address=models.CharField(max_length=300,null=True,blank=False)
    code=models.CharField(max_length=100,null=True,blank=False)
    phone=models.CharField(max_length=100,null=True,blank=False)
    email=models.CharField(max_length=300,null=True,blank=False)
    city=models.CharField(max_length=300,null=True,blank=False)
    state=models.CharField(max_length=300,null=True,blank=False)

    def __str__(self):
        return self.address








