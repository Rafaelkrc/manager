from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UnitMeasure(models.Model):
    name = models.CharField(max_length=10)
    abraviation = models.CharField(max_length=3)

    def __str__(self):
        return self.name
