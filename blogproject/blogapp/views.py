from django.shortcuts import get_object_or_404, render

from .models import Author, Blog, Category

def index(request):
    blogs = Blog.objects.all()
    context = {
        'authors' : Author.objects.all(),
        'blogs'  : blogs,
        'categories'  : Category.objects.all(),
    }    
    return render(request, 'index.html/', context = context)

def blog_detail(request, uuid):   
    if uuid:            
        blog = get_object_or_404(Blog, uuid=uuid)
        return render(request, 'blog_detail.html/', {'blog': blog})
    else:        
        return render(request, 'blog_detail.html/')