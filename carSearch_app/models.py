from django.db import models
from django.core.exceptions import  ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only Alphanumeric characters are allowed")
    return value

class Showroomlist(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    chassisnumber = models.CharField(max_length=50,  null=True, validators=[alphanumeric])
    showroom =  models.ForeignKey(Showroomlist, on_delete = models.CASCADE, related_name='showrooms', null=True)

    
    def __str__(self):
        return self.name

class Review(models.Model):
    apiuser = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comments = models.CharField(max_length = 250, null=True)
    car = models.ForeignKey(Carlist, on_delete = models.CASCADE, related_name='reviews', null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'The rating for the car ' + self.car.name + ' is ' + str(self.rating)

