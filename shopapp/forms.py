from django import forms
from django.forms import fields
from .models import Order, EmployeeInformation

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInformation
        fields = '__all__'

