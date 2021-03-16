from django.urls import path
from .views import HomePageView, detail_blog, search_blogs, tagged_blogs, send_email

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/<str:author>/<slug:slug>/', detail_blog, name='detail_blog'),
    path('search/', search_blogs, name='search_blogs'),
    path('tag/<slug:slug>/', tagged_blogs, name='tagged_blogs'),
    path('blog/send_email/<int:pk>/<str:author>/<slug:slug>/',
         send_email, name='send_email'),
]
