from django.views.generic import ListView, DetailView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs_list'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'