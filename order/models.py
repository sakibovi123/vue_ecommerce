from django.db import models

# Create your models here.

from store.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address = models.TextField(max_length=300)

    paid_amount = models.FloatField(null=True, blank=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name



class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name = "items", on_delete=models.DO_NOTHING)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)