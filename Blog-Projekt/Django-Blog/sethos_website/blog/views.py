from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")


def individualPost(request, individual_post):
    return render(request, "blog/individualpost.html")
