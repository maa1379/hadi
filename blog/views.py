from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/list.html"
