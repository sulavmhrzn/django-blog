import requests
from django.shortcuts import redirect, render, get_object_or_404 ,get_list_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from django.conf import settings
from blog.models import Blog
from blog.models import Comment
from blog.forms import CommentForm

class HomePageView(ListView):
    queryset = Blog.published.all() 
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'

def detail_blog(request, pk, author, slug):
    blog = get_object_or_404(Blog, pk=pk, author__username=author, slug=slug, status='PU')
    comments = Comment.objects.filter(blog=blog).order_by('-date_added')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            """Begin recaptcha validation"""
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            """ End recaptcha valdation"""
            if result['success']:
                add_blog = form.save(commit=False)
                add_blog.blog = blog
                add_blog.save()
                messages.success(request, 'Comment successfully added.')
                return redirect(request.path)
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again')
        else:
            messages.error(request, 'Something went wrong.')
            return redirect(request.path)

    context = {
        'blog':blog,
        'comments':comments,
        'form':form
    }
    return render(request, 'blog/detail-blog.html', context)