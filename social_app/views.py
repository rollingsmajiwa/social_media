from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.

def post_lists(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {"message": "Welcome to FriendzConnect", "posts": posts}
    return render(request, 'social/post.html', context)