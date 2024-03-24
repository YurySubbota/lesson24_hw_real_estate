from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'owner'),
        ('applicant', 'applicant')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    role = models.CharField(choices=ROLE_CHOICES, default='applicant', max_length=20)
