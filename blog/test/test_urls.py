from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import HomePageView

class TestHomePage(SimpleTestCase):
    def test_view_url_reolves_to_correct_function(self):
        url = resolve('/')
        self.assertEqual(url.func.view_class, HomePageView)