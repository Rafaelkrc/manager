from django.db import models
from products.models import Product
from base.models import User


class DispatchProduction(models.Model):
    po = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='dispatch_product')
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(unique=True)
    estimated_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='dispatch_user')
    user_update = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='dispatch_up_user')

    def __str__(self):
        return str(self.product)
