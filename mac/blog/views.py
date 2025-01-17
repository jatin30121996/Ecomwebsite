from django.shortcuts import render
from .models import Blogpost
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    return render(request, "blog/index.html", {'myposts':myposts})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, "blog/blogpost.html", {'post':post})