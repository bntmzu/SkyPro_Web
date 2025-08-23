from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import ProductForm
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = "home.html"
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.select_related("category").order_by("-created_at")


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"You have new message from {name}({email}): {message}")
        messages.success(request, "Your message has been sent successfully!")
        return redirect("catalog:contacts")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product created successfully")
        return response

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})
 
