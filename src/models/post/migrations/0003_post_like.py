# Generated by Django 2.2.1 on 2019-05-05 04:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20190504_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='count_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
