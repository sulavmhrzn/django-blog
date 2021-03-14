from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from blog.models.blog_model import Blog
class HomePageView(ListView):
    queryset = Blog.published.all() 
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'

def detail_blog(request, pk, author, slug):
    blog = get_object_or_404(Blog, pk=pk, author__username=author, slug=slug)
    return render(request, 'blog/detail-blog.html', {'blog':blog})