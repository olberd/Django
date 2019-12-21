from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=48)
