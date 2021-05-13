from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm
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
        data['unit_price'] = product_unit_price.unit_price
        data['total_price'] = product_unit_price.unit_price * int(data['quantity'])
        f = OrderForm(data)
        if f.is_valid():
            order_data = f.save()
        message = "Product Added To The Cart"
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

    # qr = qrcode.QRCode(
    #     version = 1,
    #     error_correction = qrcode.constants.ERROR_CORRECT_H,
    #     box_size = 10,
    #     border = 4,
    # )

    # The data that you want to store
    # data = "The Data that you need to store in the QR Code"

    # # Add data
    # qr.add_data(data)
    # qr.make(fit=True)

    # # Create an image from the QR Code instance
    # img = qr.make_image()
    # filename = "static/"+'lion'+".jpg"
    
    # img.save(filename)

    for order in orders:
        history = History(
            email=order.email,
            phone=order.phone,
            name=order.name,
            product=order.product,
            quantity=order.quantity
        )
        history.save()

    Order.objects.all().delete()

    context = {
        'orders': orders,
        'img': 'lion.jpg',
    }
    pdf = render_to_pdf('shopapp/invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


