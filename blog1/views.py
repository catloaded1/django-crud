from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# some_app/views.py
from django.views.generic import PostListView

class PostListView(PostListView):
    PostListView = "post"
  
from django.views.generic import PostCreateView

class PostCreateView(PostCreateView):
    PostCreateView = "post"

fields = “__all__”

success_url  = reverse_lazy(“blog:all”)

from django.views.generic import PostDeleteView

class PostDeleteView(PostDeleteView):
    PostDeleteView = "post"

fields = “__all__”

success_url  = reverse_lazy(“blog:all”)
  