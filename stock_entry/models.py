from django.db import models
from production_movements.models import ProductionMovement
from base.models import User
from employees.models import Employee
from production_sectors.models import ProductionSector


class StockEntry(models.Model):
    name = models.CharField(default='Stock Entry')
    po = models.ForeignKey(ProductionMovement, on_delete=models.PROTECT, related_name='entry_movement')
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='entry_employee')
    origin_sector = models.ForeignKey(ProductionSector, on_delete=models.PROTECT, related_name='entry_orig_sector', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='entry_user')
    user_update = models.ForeignKey(User, on_delete=models.PROTECT, auto_created=True, related_name='entry_up_user')

    def __str__(self):
        return self.name
