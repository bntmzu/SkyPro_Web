from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by("-created_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Post.objects.filter(pk=obj.pk).update(views_count=obj.views_count + 1)
        obj.refresh_from_db(fields=["views_count"])
        try:
            if obj.views_count == 100:
                subject = "Post reached 100 views"
                message = (
                    f"Congratulations! The post '{obj.title}' has reached 100 views."
                )
                from_email = (
                    getattr(settings, "DEFAULT_FROM_EMAIL", None)
                    or "no-reply@example.com"
                )
                recipient = getattr(settings, "ADMIN_EMAIL", None) or getattr(
                    settings, "DEFAULT_FROM_EMAIL", None
                )
                if recipient:
                    send_mail(
                        subject, message, from_email, [recipient], fail_silently=True
                    )
        except Exception:
            pass
        return obj


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        messages.success(self.request, "Post created successfully")
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully")
        return super().delete(request, *args, **kwargs)
