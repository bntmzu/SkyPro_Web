from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "preview", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Write content...",
                }
            ),
            "preview": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Title",
            "content": "Content",
            "preview": "Preview image",
            "is_published": "Is published",
        }


