from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from .models import Products, Order
from django.template import loader

# Create your views here.

def home(request):
    return render(request, 'shopapp/home.html')

@csrf_exempt
def order(request):
    form = OrderForm()
    message = ""
    products = Products.objects.all()
    template = loader.get_template('shopapp/order.html')
    context = {
        'products': products,
    }
    print(products)
    if request.method == "POST":
        data = request.POST
        f = OrderForm(request.POST)
        if f.is_valid():
            order_data = f.save()
        message = "Product Added To The Cart"
    return HttpResponse(template.render(context, request))

def confirm(request):
    orders = Order.objects.all()
    template = loader.get_template('shopapp/confirm.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))
