from django.db import models
from django.utils.text import slugify

# Create your models here.
class Officer(models.Model):
    fullName= models.CharField(max_length=100)
    mobno = models.CharField(max_length=10, unique=True)    
    email = models.EmailField(max_length=254, unique=True)
    address = models.TextField()  
    access=models.BooleanField(default=False)
    password= models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

# Government scheme for farmer
class Scheme(models.Model):
    title = models.CharField(max_length=50)
    titleimg = models.ImageField(upload_to='scheme_images/')
    desc = models.TextField()
    officialweb = models.URLField(blank=True, null=True)
    ytVideo = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    