import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

from blog.models import Blog
from django.contrib.auth.models import User

user = User.objects.first()

def add_data(title, main_image, content, user, status):
    data, created = Blog.objects.get_or_create(title=title,
                                            main_image=main_image,
                                            content=content,
                                            status=status, 
                                            author=user)
    print(f'Data: {data}, Created: {created}')

def populate():
    for i,_ in enumerate(range(20)):
        add_data(f'test data-{i}', f'{i}.jpg', f'test content-{i}', user, 'PU')

if __name__ == '__main__':
    populate()