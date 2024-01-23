# Generated by Django 3.2.10 on 2023-01-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='desktop_video',
            field=models.FileField(null=True, upload_to='banner_videos/desktop/', verbose_name='Banner Video for Desktop'),
        ),
        migrations.AddField(
            model_name='banner',
            name='mobile_video',
            field=models.FileField(null=True, upload_to='banner_videos/mobile/', verbose_name='Banner Video for Mobile'),
        ),
    ]
