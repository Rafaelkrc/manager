from django.db import models

TYPE_CHOICES = (('Normal', 'Normal'), ('Stock Entry', 'Stock Entry'))


class ProductionSector(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Normal')
    ordering = models.IntegerField()
