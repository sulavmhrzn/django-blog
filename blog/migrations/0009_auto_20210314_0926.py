# Generated by Django 3.1.7 on 2021-03-14 09:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210314_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
