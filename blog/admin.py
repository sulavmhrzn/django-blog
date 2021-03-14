from django.contrib import admin
from blog.models import Blog
from blog.models import Comment
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status','date_added', 'author')
    list_editable = ('status',)
    list_filter = ('status', 'date_added')
    search_fields = ('title', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'date_added')
    list_filter = ('name', 'blog', 'date_added')
    search_fields = ('name', 'blog__title')