from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField(upload_to="static/blogs_img/", default="static/blogs_img/default.jpg")
    date_created = models.DateField(auto_now=True)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title