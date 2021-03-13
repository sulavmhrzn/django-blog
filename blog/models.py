from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'PU')
class Blog(models.Model):
    STATUS = (
        ('PU', 'published'),
        ('DR', 'draft')
    )
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(editable=False, unique=True, null=True)
    main_image = models.ImageField(upload_to='image',null=True)
    content = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=2, choices=STATUS,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    published = PublishedManager()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('detail_blog', kwargs = {
            'pk':self.pk,
            'author':self.author,
            'slug':self.slug
        })

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)