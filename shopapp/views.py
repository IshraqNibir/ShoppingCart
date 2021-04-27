from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'shopapp/home.html')

def order(request):
    return render(request, 'shopapp/order.html')