from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from blog.models import Blog
from blog.models import Comment
from blog.forms import CommentForm
from blog.forms import SendEmailForm
from blog.decorators.recaptcha import check_recaptcha


class HomePageView(ListView):
    queryset = Blog.published.all().order_by('-date_added')
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 10


def search_blogs(request):
    title = request.GET.get('title', '')
    blogs = None
    if title:
        blogs = Blog.published.filter(
            title__icontains=title).order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blog/search-blogs.html', context)


def tagged_blogs(request, slug):
    blogs = Blog.published.filter(tags__slug__in=[slug]).distinct()
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'blogs': blogs,
        'slug': slug,
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'blog/tagged-blogs.html', context)


@check_recaptcha
def detail_blog(request, pk, author, slug):
    blog = get_object_or_404(
        Blog, pk=pk, author__username=author, slug=slug, status='PUB')
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
        'blog': blog,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/detail-blog.html', context)


def send_email(request, pk, author, slug):
    blog = get_object_or_404(
        Blog, pk=pk, author__username=author, slug=slug, status='PUB')
    form = SendEmailForm()
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('your_name')
            email = form.cleaned_data.get('email')
            send_mail(subject=f'{name} shared you a blog posts.',
                      message=f'To view the post visit {request.scheme}://{request.get_host()}{blog.get_absolute_url()}',
                      from_email='admin@sm.com',
                      recipient_list=[email],
                      fail_silently=False
                      )
            messages.success(request, 'Email was successfully sent.')
            return redirect(blog.get_absolute_url())
        else:
            messages.error(
                request, 'Something went wrong during sending email.', extra_tags='danger')
            return redirect(blog.get_absolute_url())

    context = {
        'form': form
    }
    return render(request, 'blog/send-email.html', context)
