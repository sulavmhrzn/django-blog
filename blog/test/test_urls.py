from django.test import SimpleTestCase
from django.urls import resolve
from blog.views import HomePageView

class TestHomePage(SimpleTestCase):
    def test_url_resolves_to_correct_view_function(self):
        url = resolve('/')
        self.assertEqual(url.func.view_class, HomePageView)
    
