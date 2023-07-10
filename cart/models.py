from django.db import models
from inventory.models  import Product
class Cart(models.Model):
    products=models.ManyToManyField(Product)
    # python3 makemigrations cart
    # python3 manage.py migrate
    # python3 manage.py runserver
    customer_ID = models.IntegerField()
    list_of_items = models.IntegerField()
    quantity_of_items = models.CharField(max_length=6)