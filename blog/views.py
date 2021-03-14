from django.shortcuts import redirect, render, get_object_or_404 
from django.views.generic.list import ListView
from django.contrib import messages
from blog.models import Blog
from blog.models import Comment
from blog.forms import CommentForm
from blog.decorators.recaptcha import check_recaptcha
class HomePageView(ListView):
    queryset = Blog.published.all().order_by('-date_added') 
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10

@check_recaptcha
def detail_blog(request, pk, author, slug):
    blog = get_object_or_404(Blog, pk=pk, author__username=author, slug=slug, status='PUB')
    comments = Comment.objects.filter(blog=blog).order_by('-date_added')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            add_blog = form.save(commit=False)
            add_blog.blog = blog
            add_blog.save()
            messages.success(request, 'Comment successfully added.')
            return redirect(request.path)
        else:
            messages.error(request, 'Something went wrong.')
            return redirect(request.path)
    else:
        form = CommentForm()
    
    context = {
        'blog':blog,
        'comments':comments,
        'form':form
    }
    return render(request, 'blog/detail-blog.html', context)