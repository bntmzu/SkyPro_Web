from django.urls import path

from catalog.views import contacts, home, product_create, product_detail

from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("products/new/", product_create, name="product_create"),
]
