from django.shortcuts import render
from django.views import View
from .models import Product

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

