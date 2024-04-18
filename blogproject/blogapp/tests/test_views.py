import uuid
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from blogapp.models import Blog, Author, Category

def setUpBlogDetails(self):
    self.author = Author.objects.create(name="Test Author")
    self.category = Category.objects.create(name="Test Category")
    self.blog = Blog.objects.create(
            author=self.author,
            category=self.category,
            article="Test Article",
            article_title="Test Title",
            date_of_publish=timezone.now().date()
        )
       
class IndexViewTest(TestCase):
    def setUp(self):
        setUpBlogDetails(self)

    def test_index_view_status_code(self):
        response = self.client.get(reverse('blogapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse('blogapp:index'))
        self.assertTemplateUsed(response, 'index.html/')

    def test_index_view_context(self):
        response = self.client.get(reverse('blogapp:index'))
        self.assertIn('authors', response.context)
        self.assertIn('blogs', response.context)
        self.assertIn('categories', response.context)
        self.assertEqual(len(response.context['authors']), Author.objects.count())
        self.assertEqual(len(response.context['blogs']), Blog.objects.count())
        self.assertEqual(len(response.context['categories']), Category.objects.count())

class BlogDetailViewTest(TestCase):
    def setUp(self):
        setUpBlogDetails(self)
        
    def test_blog_detail_view_with_valid_uuid(self):
        response = self.client.get(reverse('blogapp:blog_detail', args=[self.blog.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html/')
        self.assertIn('blog', response.context)
        self.assertEqual(response.context['blog'], self.blog)

    def test_blog_detail_view_with_invalid_uuid(self):
        invalid_uuid = str(uuid.uuid4())
        response = self.client.get(reverse('blogapp:blog_detail', args=[invalid_uuid]))
        self.assertEqual(response.status_code, 404)