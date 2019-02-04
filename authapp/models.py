from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='аватарка', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')


