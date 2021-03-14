from django.urls import path
from .views import HomePageView, detail_blog, search_blogs

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/<str:author>/<slug:slug>/', detail_blog, name='detail_blog'),
    path('search/', search_blogs, name='search_blogs')
]