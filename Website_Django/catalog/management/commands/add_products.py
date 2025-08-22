from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category
from decimal import Decimal

class Command(BaseCommand):
    help = 'Add test products to database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        self.stdout.write("Loading products from fixture...")
        call_command('loaddata', 'catalog/fixtures/products.json')

        self.stdout.write(self.style.SUCCESS("New test products successfully loaded."))
