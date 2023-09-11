from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from cart.models import Cart
from order.models import Order



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = "__all__"


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = "__all__"

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"