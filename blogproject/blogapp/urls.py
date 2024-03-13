from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:title>/<str:author>/', views.blog_detail, name='blog_detail'),

]
