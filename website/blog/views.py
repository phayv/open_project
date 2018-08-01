from django.views import generic
from .models import Post


class IndexView(generic.list.ListView):
    template_name = 'blog/blog.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Portfolio"
        context['title'] = 'Portfolio Page'
        return context

    def get_queryset(self):
        return Post.objects.order_by("-date")[:5]


class PostDetailView(generic.detail.DetailView):
    template_name = "blog/post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_ids'] = [x.id for x in Post.objects.order_by("id")]
        context['min'] = min(context['list_of_ids'])
        context['max'] = max(context['list_of_ids'])

        context['previous_post_id'] = int(self.kwargs['pk']) - 1
        context['next_post_id'] = int(self.kwargs['pk']) + 1

        context['post_pic_file'] = 'blog/img/{}.jpg'.format(self.kwargs['pk'])

        return context
