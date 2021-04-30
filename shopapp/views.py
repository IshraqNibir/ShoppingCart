from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'shopapp/home.html')

@csrf_exempt
def order(request):
    form = OrderForm()
    message = ""
    if request.method == "POST":
        data = request.POST
        f = OrderForm(request.POST)
        if f.is_valid():
            order_data = f.save()
        message = "Product Added To The Cart"
    return render(request, 'shopapp/order.html', {"message": message})