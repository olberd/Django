from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название', max_length=80, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=125)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=100, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
