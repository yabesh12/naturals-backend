# Generated by Django 3.2.10 on 2023-01-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='desktop_image',
            field=models.ImageField(null=True, upload_to='bridal_gallery/desktop/', verbose_name='Our Services Image for Desktop'),
        ),
        migrations.AddField(
            model_name='service',
            name='mobile_image',
            field=models.ImageField(null=True, upload_to='bridal_gallery/mobile/', verbose_name='Our Services Image for Mobile'),
        ),
    ]
