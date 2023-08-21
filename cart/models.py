from django.db import models
from inventory.models  import Product
class Cart(models.Model):
    class Meta:
       verbose_name_plural = "Product_cart"
    products = models.ManyToManyField(Product)
    product_name = models.CharField(max_length=32)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image= models.ImageField()
    date_added = models.DateTimeField()
    # products=models.ManyToManyField(Product)
    # customer_ID = models.IntegerField()
    # list_of_items = models.IntegerField()
    # quantity_of_items = models.CharField(max_length=6)