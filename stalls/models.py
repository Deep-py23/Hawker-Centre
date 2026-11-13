from django.db import models
from accounts.models import User
from django.conf import settings 
from django.db.models import UniqueConstraint


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Stall(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    stall_number = models.CharField(max_length=10, unique=True)
    is_open = models.BooleanField(default=False)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT, 
        limit_choices_to={'role': User.Role.OWNER},
        related_name='stall')
    
    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to= 'dishes/', blank=True)
    is_available = models.BooleanField(default=True)
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE, related_name='dishes')
    category = models.ForeignKey(Category, 
                                 on_delete= models.SET_NULL, 
                                 null=True, blank=True,
                                 related_name='dishes')


    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name', 'stall'],
                name="unique_dish_name_per_stall",
            ),
        ]


    def __str__(self):
        return self.name