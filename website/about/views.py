from django.views import generic
from blog.models import Post


class IndexView(generic.list.ListView):
    template_name = 'about/index.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "About"
        context['title'] = 'About Me'
        return context

    def get_queryset(self):
        return Post.objects.order_by("-date")[:5]