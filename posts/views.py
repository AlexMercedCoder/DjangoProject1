from django.shortcuts import render
from django.http import HttpResponse
from .models import posts


# Create your views here.
def index(request):
#    return HttpResponse('Hello from Posts')

    blogpost = posts.objects.all()[:10]

    context = {
        'title': 'latest posts',
        'posts': blogpost
    }

    return render(request, 'posts/index.html', context)

def details (request, id):
    blogposts = posts.objects.get(id=id)

    context = {'posts': blogposts}

    return render(request, 'posts/details.html', context)
