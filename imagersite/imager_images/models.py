from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


# Create your models here.
class Photo(models.Model):
    """this the the Photo model"""
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=180, default="Untitled")
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    image = ImageField(upload_to="images")
    published = models.CharField(max_length=7, choices=(('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')))

    def __str__(self):
        return '{}'.format(self.title)


class Album(models.Model):
    """this is the model Album model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    cover = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    title = models.CharField(max_length=180, default="Untitled")
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(max_length=7, choices=(('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')))

    def __str__(self):
        return '{}'.format(self.title)