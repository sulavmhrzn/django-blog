from blog.models import Blog

def get_recent_blog_posts(request):
    blogs = Blog.published.order_by('-date_added')[:3]
    return {
        'recent_blogs':blogs
    }