from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('confirm', views.confirm, name='confirm'),
    path('employee_information', views.employee_information, name='employee_information'),
    path('get_invoice', views.get_invoice, name='get_invoice'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)