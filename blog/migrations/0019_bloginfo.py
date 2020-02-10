# Generated by Django 2.2.7 on 2019-12-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191225_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='PGSM', max_length=50)),
                ('logo', models.ImageField(upload_to='blog/article-category-cover')),
            ],
        ),
    ]