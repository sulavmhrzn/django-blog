from django.template.defaultfilters import title
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.views import detail_blog
from blog.models import Blog
class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_view_GET(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogs.html')

class TestDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@user.com', 'testpassword')
        self.test_blog = Blog.objects.create(
            title='test one',
            main_image = '1.jpg', 
            content = 'test content',
            status = 'PU',
            author = self.user
        )

    
    def test_view_GET(self):
        response = self.client.get(reverse('detail_blog', kwargs={'pk':self.test_blog.id,
                                                                'author':self.test_blog.author, 
                                                                'slug':self.test_blog.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail-blog.html')