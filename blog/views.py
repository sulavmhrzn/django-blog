from django.db.models import query
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Blog
class HomePageView(ListView):
    queryset = Blog.published.all() 
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'