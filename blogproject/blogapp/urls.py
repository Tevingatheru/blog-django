from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:uuid>/', views.blog_detail, name='blog_detail'),

]
