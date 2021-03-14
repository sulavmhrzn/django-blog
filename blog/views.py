from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from blog.models.blog_model import Blog
from blog.forms import CommentForm

class HomePageView(ListView):
    queryset = Blog.published.all() 
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'

def detail_blog(request, pk, author, slug):
    blog = get_object_or_404(Blog, pk=pk, author__username=author, slug=slug)
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            add_blog = form.save(commit=False)
            add_blog.blog = blog
            add_blog.save()
            messages.success(request, 'Comment successfully added.')
            return redirect(request.path)
        else:
            messages.error(request, 'Something went wrong.')
            return redirect(request.path)

    context = {
        'blog':blog,
        'form':form
    }
    return render(request, 'blog/detail-blog.html', context)