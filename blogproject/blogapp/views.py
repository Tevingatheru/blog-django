from django.shortcuts import render

from blogproject.blogapp.models import Author, Blog, Category

# Create your views here.
def index(request):
    context = {
        'all_authors' : Author.objects.all(),
        'all_blogs'  : Blog.objects.all(),
        'all_categories'  : Category.objects.all(),
    }
    return render(request, 'blogapp/index.html')