from django.views import generic
from .models import Product


class IndexView(generic.list.ListView):
    template_name = 'blog/blog.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.order_by("-date")[:5]
