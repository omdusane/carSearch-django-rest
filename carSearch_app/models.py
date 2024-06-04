from django.db import models

class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    chassisnumber = models.CharField(max_length=50,  null=True)
