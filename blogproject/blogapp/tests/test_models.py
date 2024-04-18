from django.test import TestCase
from django.utils import timezone
from blogapp.models import Author, Blog, Category
import uuid

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")

    def test_author_str(self):
        self.assertEqual(str(self.author), "Test Author")

    def test_author_uuid_default(self):
        self.assertIsInstance(self.author.uuid, uuid.UUID)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_category_uuid_default(self):
        self.assertIsInstance(self.category.uuid, uuid.UUID)

class BlogModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.category = Category.objects.create(name="Test Category")
        self.blog = Blog.objects.create(
            author=self.author,
            category=self.category,
            article="Test Article",
            article_title="Test Title",
            date_of_publish=timezone.now().date()
        )

    def test_blog_str(self):
        expected_object_name = f'{self.blog.article_title} : {self.blog.date_of_publish} - {self.blog.uuid}'
        self.assertEqual(str(self.blog), expected_object_name)

    def test_blog_uuid_default(self):
        self.assertIsInstance(self.blog.uuid, uuid.UUID)

    def test_blog_author_relationship(self):
        self.assertEqual(self.blog.author, self.author)

    def test_blog_category_relationship(self):
        self.assertEqual(self.blog.category, self.category)