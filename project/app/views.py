from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import UserRegistration
from django.contrib.auth.models import User

# Create your views here.

class Product_view(View):
      
    def get_context_data(self):
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, 'Home.html', context)
    
    
class Login_view(View):
    template_name = 'Login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    
class Signup_view(View):
    template_name = 'signup.html'
    
    def get(self, request):
        form = UserRegistration()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                user.save()
                return redirect(request, 'login')
            
        context = {'form':form}
        return render(request, self.template_name, context)
        

