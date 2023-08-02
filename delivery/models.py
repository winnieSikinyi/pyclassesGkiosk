from django.db import models
from customer.models import Customer

# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=32)
    customer_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.TextField()
    deliver_status = models.CharField(max_length=16)

class Meta:
    verbose_name = 'Delivery'
    verbose_name_plural = 'Deliveries'    