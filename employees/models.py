from django.db import models
from states.models import City, State, Country
from production_sectors.models import ProductionSector


class Employee(models.Model):
    register = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    adress_number = models.CharField(max_length=5)
    neighbourhood = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='employee_city')
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='employee_state')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='employee_country')
    email = models.EmailField()
    production_sector = models.ManyToManyField(ProductionSector, related_name='employee_sector', blank=True)

    def __str__(self):
        return self.name
