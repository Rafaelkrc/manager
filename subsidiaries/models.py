from django.db import models
from organization.models import Organization
from states.models import City, State, Country


class Subsidiary(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='subsidiaries', default=1)
    register = models.CharField(max_length=20, unique=True,)
    name = models.CharField(max_length=200)
    fantasy_name = models.CharField(max_length=200)
    adress = models.CharField(max_length=250)
    number_adress = models.CharField(max_length=5)
    neighbourhood = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='subsidiary_city')
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='subsidiary_state')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='subsidiary_country')
    email = models.EmailField(blank=True, null=True)
    date_of_fundation = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='organization/', blank=True, null=True)

    def __str__(self):
        return self.name