# Generated by Django 3.1.7 on 2021-03-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
    ]
