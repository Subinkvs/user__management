from django.urls import path
from .views import *

urlpatterns = [
    
    path('', Product_view.as_view(), name="product_view"),
    path('login/',Login_view.as_view(), name="login" ),
    path('signup/',Signup_view.as_view(), name="signup" )
    
]
