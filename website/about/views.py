from django.views import generic
from blog.models import Post


class IndexView(generic.list.ListView):
    template_name = 'about/index.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "About"
        context['title'] = 'About Me'
        context['paragraph'] = """
            Hello, \n\n
            My name is Phay and I am a Math and Physics major graduate from the University of California, Irvine. \
            I created this website from scratch using Python Django and PostgreSQL for the database.\n\n\
            I've always had a knack for interior design, but I think I have a small gift to go along with my \
            knowledge of interior design. When I close my eyes, I can imagine a room I have been in before. Then \
            in my mind, I can add to the room or remove things from it. \n\n \
            Then I can imagine walking around the room from my own perspective and make more changes accordingly.\n\n
        """
        return context

    def get_queryset(self):
        return Post.objects.order_by("-date")[:5]

