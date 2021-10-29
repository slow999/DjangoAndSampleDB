from django.db import models


# Create your models here.
class Order(models.Model):
    region = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=128, blank=True)
    item_type = models.CharField(max_length=64, blank=True)
    sales_channel = models.CharField(max_length=32, blank=True)
    order_priority = models.CharField(max_length=8, blank=True)
    order_date = models.DateField(null=True)
    order_id = models.IntegerField(null=True)
    ship_date = models.DateField(null=True)
    units_sold = models.IntegerField(null=True)
    unit_price = models.DecimalField(null=True, max_digits=8, decimal_places=2)
    unit_cost = models.DecimalField(null=True, max_digits=8, decimal_places=2)
    total_revenue = models.DecimalField(null=True, max_digits=16, decimal_places=2)
    total_cost = models.DecimalField(null=True, max_digits=16, decimal_places=2)
    total_profit = models.DecimalField(null=True, max_digits=16, decimal_places=2)

