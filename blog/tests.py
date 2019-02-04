from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Blog


class BlogModelTests(TestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='testpass',
        )

        self.blog = Blog.objects.create(
            title='testtitle',
            author=self.author,
            text='test text',
        )
        self.client = Client()
    
    def test_string_representation(self):
        blog = Blog(title='A nice title')
        self.assertEqual(str(blog), blog.title)
    
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'testtitle')
        self.assertEqual(f'{self.blog.author}', 'testuser')
        self.assertEqual(f'{self.blog.text}', 'test text')
    
    def test_blog_list_view(self):
        res = self.client.get(reverse('home'))

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'test text')
        self.assertTemplateUsed(res, 'home.html')
    
    def test_blog_detail_view(self):
        res = self.client.get('/blog/1')
        no_res = self.client.get('/blog/10')

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'testtitle')
        self.assertTemplateUsed(res, 'blog_detail.html')
        self.assertEqual(no_res.status_code, 404)

