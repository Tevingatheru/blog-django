from django.contrib import admin
from .models import Author, Blog, Category

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):    
    list_filter = ('name', 'date_registered')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_filter =  ('author', 'article_title', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter  = ('name', )