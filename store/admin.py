from django.contrib import admin
from .models import Category, Book

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'in_stock', 
                    'is_active', 'created', 'updated', 'image']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock']
    prepopulated_fields = {'slug': ('title',)}
