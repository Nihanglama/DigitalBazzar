from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from DigitalBazzar.forms import Signup
from DigitalBazzar.models import Customer



class Login(LoginView):
    template_name='user_handler/login.html'
    fields='__all__'
    
    def get_success_url(self):
        return reverse_lazy('products')

    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            self.cus=self.request.user.customer.name
            return redirect('products')
        return super(Login,self).get( *args, **kwargs)
        

def register(request):
    if request.user.is_authenticated:
        return redirect('products')
    form=Signup
    template_name="user_handler/register.html"
    if request.method=="POST":
        form=Signup(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')
    context_object_name={'form':form}
    return render(request,template_name,context_object_name)




