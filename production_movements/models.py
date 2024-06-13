from django.db import models
from dispatch_production.models import DispatchProduction
from base.models import User
from production_sectors.models import ProductionSector
from employees.models import Employee


class ProductionMovement(models.Model):
    po = models.ForeignKey(DispatchProduction, on_delete=models.PROTECT, related_name='movement_dispatch')
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='movement_employee')
    origin_sector = models.ForeignKey(ProductionSector, on_delete=models.PROTECT, related_name='movement_orig_sector', default=0)
    priority = models.ForeignKey(DispatchProduction, on_delete=models.PROTECT, related_name='movement_priority_dispatch', default=0)
    destynation_sector = models.ForeignKey(ProductionSector, on_delete=models.PROTECT, related_name='movement_dest_sector', default=0)
    destynation_employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='movement_dest_employee', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='movement_user', blank=True, null=True)
    user_update = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='movement_up_user', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.po)
