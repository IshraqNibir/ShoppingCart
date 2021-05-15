from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Order, EmployeeInformation
from .forms import OrderForm, EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from .models import Products, Order, History
from django.template import loader
from django.views.generic import View
from .utils import render_to_pdf
import datetime
import qrcode
import qrcode.image.svg
from io import BytesIO
from barcode.writer import SVGWriter
import base64
import random

increment = 1

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
    if request.method == "POST":
        if not request.POST._mutable:
            request.POST._mutable = True
        data = request.POST
        post_product = data.get('product')
        product_unit_price = Products.objects.get(product_name=post_product)
        if product_unit_price.quantity < int(data.get('quantity')):
            context['message'] = "Stock Shortage!! The Quantity Of The Selected Product Must Be Less Than " + str(product_unit_price.quantity)
            return HttpResponse(template.render(context, request))

        data['unit_price'] = product_unit_price.unit_price
        data['total_price'] = product_unit_price.unit_price * int(data['quantity'])
        f = OrderForm(data)
        if f.is_valid():
            order_data = f.save()
    return HttpResponse(template.render(context, request))

def confirm(request):
    orders = Order.objects.all()
    template = loader.get_template('shopapp/confirm.html')
    if request.method == "POST":
        for order in orders:
            history = History(
                email=order.email,
                phone=order.phone,
                name=order.name,
                product=order.product,
                quantity=order.quantity
            )
            history.save()
        return redirect('get_invoice')

    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))


def get_invoice(request,  *args, **kwargs):
    orders = Order.objects.all()
    employee = EmployeeInformation.objects.first()

    if request.method == 'GET':
        print("Hello Nibir")

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 6,
        border = 4,
    )

    # The data that you want to store
    data = "Name : " + employee.name + "\n" + "Phone: " + employee.phone + "\n" + "Email: " + employee.email

    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # # Create an image from the QR Code instance
    img = qr.make_image()
    ran_int = random.randint(1, 10000000)
    filename = "static/" + employee.phone + str(ran_int) + ".jpg"
    print(filename)
    
    img.save(filename)

    for order in orders:
        history = History(
            email=employee.email,
            phone=employee.phone,
            name=employee.name,
            product=order.product,
            quantity=order.quantity
        )
        history.save()

    Order.objects.all().delete()

    context = {
        'orders': orders,
        'img': employee.phone + str(ran_int) + '.jpg',
    }
    pdf = render_to_pdf('shopapp/invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def employee_information(request):
    if request.method == 'POST':
        EmployeeInformation.objects.all().delete()
        data = request.POST
        employeeform = EmployeeForm(data)
        if employeeform.is_valid():
            employeeform.save()
            return redirect('order')
    return render(request, 'shopapp/employee.html')