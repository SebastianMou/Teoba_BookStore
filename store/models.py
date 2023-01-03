from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Mate:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    descripttion = models.TextField()
    image = models.ImageField(upload_to='images/', default='imagess/default.png')
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    lod_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    year = models.IntegerField(null=True)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
    
    def __str__(self) -> str:
        return self.title