import datetime
import os

from cart.cart import Cart
from order.models import Order, OrderItems

def checkout(request, first_name, last_name, city, address, zip_code):
    order = Order(first_name=first_name, last_name=last_name, city=city, address=address, zip_code=zip_code)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItems.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

    return order.id