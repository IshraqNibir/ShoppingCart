from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('confirm', views.confirm, name='confirm'),
]