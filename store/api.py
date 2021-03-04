from django.shortcuts import get_object_or_404

from cart.cart import Cart
from .models import Product

from django.http import JsonResponse

import json

from order.utils import checkout
from order.models import Order, OrderItems

def api_for_add_to_cart(request):
    jsonresponse = {'success': True}
    data = json.loads(request.body)
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, updated_quantity=False)
    else:
        cart.add(product=product, quantity=quantity, updated_quantity=True)

    return JsonResponse(jsonresponse)





def api_remove_from_cart(request):
    cart = Cart(request)
    jsonresponse = {'Removed': True}

    data = json.loads(request.body)

    product_id = str(data['product_id'])

    cart.remove(product_id)

    return JsonResponse(jsonresponse)


def api_checkout(request):
    cart = Cart(request)
    jsonresponse = {'Success': True}

    data = json.loads(request.body)

    first_name = data['first_name']
    last_name = data['last_name']
    city = data['city']
    address = data['address']
    zip_code = data['zip_code']

    orderId = checkout(request, first_name, last_name, city, address, zip_code)

    paid = True

    if paid == True:
        order = Order.objects.get(pk=orderId)

        order.paid = True
        order.paid_amount = cart.get_total_cost()

        order.save()
        cart.clear()
    return JsonResponse(jsonresponse)





