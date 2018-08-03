from django.views import generic
from blog.models import Post


class IndexView(generic.list.ListView):
    template_name = 'contact/index.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Contact"
        context['title'] = 'Contact Us'
        context['form_title'] = 'Please Provide Your Information'
        context['paragraph'] = """
            To speak with Phay about your project, please submit this form and we will get back to you right away to schedule a call.
        """
        return context

    def get_queryset(self):
        pass

