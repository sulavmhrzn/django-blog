from django.contrib import admin
from blog.models.blog_model import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status','date_added')
    list_editable = ('status',)
    list_filter = ('status', 'date_added')