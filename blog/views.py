from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs_list'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'author', 'text']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')