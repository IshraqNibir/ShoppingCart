from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(blank=False)
    product_code = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=200, blank=False)
    unit_price = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    product = models.CharField(max_length=100, blank=False)
    quantity = models.PositiveIntegerField(blank=False)
    unit_price = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

class History(models.Model):
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=100, blank=False)
    product = models.CharField(max_length=100, blank=False)
    quantity = models.PositiveIntegerField(blank=False)


class EmployeeInformation(models.Model):
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=100, blank=False)