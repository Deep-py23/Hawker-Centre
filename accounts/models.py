from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'customer', 'Customer'
        OWNER = 'owner', 'Stall Owner'
        ADMIN = 'admin', 'Admin'


    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    phone = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.username

