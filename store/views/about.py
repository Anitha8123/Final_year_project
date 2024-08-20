from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class About(View):
    def get(self , request):
        
        return render(request , 'about.html'  )

