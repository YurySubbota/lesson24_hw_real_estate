from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CityDistrict(models.Model):
    city_district = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.city_district


class Metro(models.Model):
    metro_station = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.metro_station


class RealEstate(models.Model):
    TYPE_OF_DEAL_CHOICE = (
        ('rent', 'rent'),
        ('sale', 'sale')
    )

    BATHROOM_CHOICE = (
        ('combined', 'combined'),
        ('separate', 'separate'),
        ('several', 'several')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    city_district = models.ForeignKey(CityDistrict, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    metro = models.ForeignKey(Metro, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    street = models.CharField(max_length=120)
    building_number = models.CharField(max_length=120)
    floors_in_house = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    area_of_premise = models.PositiveSmallIntegerField()
    type_of_deal = models.CharField(choices=TYPE_OF_DEAL_CHOICE, default='sale', max_length=100)
    bathroom = models.CharField(choices=BATHROOM_CHOICE, default='combined', max_length=100)
    balcony = models.BooleanField(default=False)
    title_photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)


class DealRequest(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    suggest_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
