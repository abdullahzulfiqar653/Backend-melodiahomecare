from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
# Create your models here.


class Blog(models.Model):
    blog_name = models.CharField(max_length=250)
    blog_image = models.ImageField(
        upload_to='blog_uploads/', blank=True, null=True)
    blog = RichTextField()

    def __str__(self):
        return self.blog_name + "_Blog"
