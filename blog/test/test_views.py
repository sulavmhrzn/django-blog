from typing import List
from django.test import TestCase
from django.test import Client
from django.urls import reverse

class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_view_GET(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogs.html')