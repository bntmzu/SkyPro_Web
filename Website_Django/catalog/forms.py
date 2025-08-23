from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "picture",
            "category",
            "price",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Description",
                }
            ),
            "picture": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "price": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "0.00", "inputmode": "decimal"}
            ),
        }

