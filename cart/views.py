from django.shortcuts import render
from .cart import Cart
# from store.models import Product


def cart_details(request):
    cart = Cart(request)
    productString = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'name': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," %(product.id, product.name, product.price, item['quantity', item['total_price']])

        productString = productString + b

    args = {'cart': cart, 'productString': productString}
    # args = {'cart': cart}
    return render(request, 'cart.html', args)
