from django.shortcuts import render

def index(request):
    context = {
        'name_var' : "Homepage",
        'page_title' : 'Welcome to the Homepage',

    }
    return render(request, 'homepage/index.html', context)
