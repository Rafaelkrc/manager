from django.db import models
from organization.models import Organization
from subsidiaries.models import Subsidiary
from product_caracteristics.models import Group, Brand, UnitMeasure
from production_sectors.models import ProductionSector
from base.models import User


class Product(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, default=1, related_name='product_organization')
    subsidiary = models.ForeignKey(Subsidiary, on_delete=models.PROTECT, default=1, related_name='product_subsidiary')
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=150)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='product_group', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand', blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT, related_name='product_unit')
    quantity = models.IntegerField(default=0)
    production_time = models.TimeField(blank=True, null=True)
    average_production_time = models.TimeField(blank=True, null=True)
    production_sectors = models.ManyToManyField(ProductionSector, related_name='product_sector')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='product_user')
    user_update = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='product_up_user')

    def __str__(self):
        return self.name
