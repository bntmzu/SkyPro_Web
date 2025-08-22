from decimal import Decimal

from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to database"

    def handle(self, *args, **kwargs):
        # Clean existing data (products first due to FK), then categories
        self.stdout.write("Clearing products and categories...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Load categories first to satisfy FK constraints, then products
        self.stdout.write("Loading categories from fixture...")
        call_command("loaddata", "catalog/fixtures/categories.json")

        self.stdout.write("Loading products from fixture...")
        call_command("loaddata", "catalog/fixtures/products.json")

        self.stdout.write(
            self.style.SUCCESS("Categories and products successfully loaded.")
        )
