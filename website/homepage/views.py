from django.shortcuts import render
from blog.models import Post


def index(request):
    context = {
        'first_three' : Post.objects.order_by('-id')[:3],
    }
    return render(request, 'homepage/index.html', context)
