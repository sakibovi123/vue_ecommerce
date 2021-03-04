from django.conf import settings

from store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart



    def __iter__(self):
        product_ids = self.cart.keys()

        cart_products = []

        for p in product_ids:
            cart_products.append(p)

            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())



    def add(self, product, quantity=1, updated_quantity=False):
        product_id = str(product.id)

        price = product.price

        print('product_id:', product_id)


        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}

        if updated_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.car[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1


        self.save()


    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True



    def get_total_quantity(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_cost(self):
        return sum(float(item['total_price']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True













