from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=2, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='region_state')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='county_state')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=70)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='state_city')

    def __str__(self):
        return self.name
