from django.views import generic
from .models import Product


class IndexView(generic.list.ListView):
    template_name = 'products/index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.order_by("sku")[:5]


class ProductDetailView(generic.detail.DetailView):
    template_name = "products/product.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Product.objects.get(id=self.kwargs['pk'])
        return context