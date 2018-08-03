from django.views import generic
from blog.models import Post


class IndexView(generic.list.ListView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Homepage"
        context['title'] = 'Welcome to the Homepage'
        context['first_three'] = Post.objects.order_by('-id')[:3]
        return context

    def get_queryset(self):
        return Post.objects.order_by("-date")[:3]
