# Generated by Django 2.2 on 2019-12-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_profile_fb_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(blank=True, upload_to='user/cover-pic', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fb_link',
            field=models.CharField(blank=True, max_length=250, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='user/profile-pic', verbose_name='Avatar'),
        ),
    ]