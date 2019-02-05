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
    
    def test_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/blog/1')
    
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

    def test_blog_create_view(self):
        res = self.client.post(reverse('blog_new'), {
            'title': 'new title',
            'text': 'new text',
            'author': self.author,
        })

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'new title')
        self.assertContains(res, 'new text')
    
    def test_blog_update_view(self):
        res = self.client.post(reverse('blog_edit', args=['1']), {
            'title': 'Updated title',
            'text': 'Updated text',
        })

        self.assertEqual(res.status_code, 302)
    
    def test_blog_delete_view(self):
        res = self.client.get(reverse('blog_delete', args=['1']))

        self.assertEqual(res.status_code, 200)