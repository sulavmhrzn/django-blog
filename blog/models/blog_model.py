from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from tinymce.models import HTMLField
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'PUB')
class Blog(models.Model):
    PUBLISHED = 'PUB'
    DRAFT = 'DRA'
    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(editable=False, null=True)
    main_image = models.ImageField(upload_to='image', null=True, blank=True)
    content = HTMLField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=3, choices=STATUS, default=DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    published = PublishedManager()
    hit_count_generic = GenericRelation(HitCount,
                                    object_id_field='object_pk',
                                    related_query_name='hit_count_generic_relation') 

    def get_absolute_url(self):
        return reverse('detail_blog', kwargs = {
            'pk':self.pk,
            'author':self.author,
            'slug':self.slug
        })

    @property
    def get_read_time(self):
        import math
        import re
        clean = re.compile('<.*?>')
        c = re.sub(clean, '', self.content)
        word_length = len(c.split())
        calc = math.ceil(word_length / 200)
        return f'{calc} minutes' if calc > 1 else f'{calc} minute'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
