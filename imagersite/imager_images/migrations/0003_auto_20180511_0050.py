# Generated by Django 2.0.4 on 2018-05-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20180425_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='albums',
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo'),
        ),
    ]