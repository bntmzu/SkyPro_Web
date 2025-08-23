from django.urls import path

from catalog.views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDetailView,
)

from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/new/", ProductCreateView.as_view(), name="product_create"),
]
