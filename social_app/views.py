from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm

# Create your views here.

def post_lists(request):
    posts = Post.objects.all().order_by('-created_on')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            if request.user.is_authenticated:
                new_post.author = request.user
            new_post.save()
            return redirect('post_list')

    context = {"form": form, "posts": posts}
    return render(request, 'social/post.html', context)