from django.shortcuts import render
from .models import Myblog
# Create your views here.

def blog_page(request):
    blogs = Myblog.objects
    return  render(request,'blog.html',{'blogs': blogs})
