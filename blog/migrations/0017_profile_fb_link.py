# Generated by Django 2.2 on 2019-12-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_link',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]