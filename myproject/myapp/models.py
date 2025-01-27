from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    stock_status = models.BooleanField(default=True)
    discount_available = models.BooleanField(default=False)
    description = models.TextField()
    photo = models.ImageField(upload_to="product_photos/", null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
