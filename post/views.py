from django.shortcuts import render
from django.views.generic import ListView, DetailView

from post.models import post2


class postList(ListView):
    model = post2
    template_name = 'post/pagination.html'
    context_object_name = 'data'


class PostDetail(DetailView):
    model = post2
    template_name = 'post/news_detail.html'
    context_object_name = 'data1'

