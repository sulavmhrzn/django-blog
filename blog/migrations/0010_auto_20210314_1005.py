# Generated by Django 3.1.7 on 2021-03-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210314_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('PU', 'published'), ('DR', 'draft')], default='DR', max_length=2),
        ),
    ]
