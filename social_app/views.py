from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
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
            return redirect('post_lists')

    context = {"form": form, "posts": posts}
    return render(request, 'social/post.html', context)

def post_details(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.author = request.user
                comment.save()
                return redirect('post_details', pk=pk)
    else:

        form = CommentForm()

    context = {
        "post": post,
        "form": form
    }
    return render(request, "social/post_details.html", context)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    #  only the author can edit
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'social/post_edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    #  only the author can delete
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('post_lists')

    return render(request, 'social/post_delete_confirm.html', {'post': post})


# --- COMMENT DELETE ---

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk

    if comment.author != request.user and comment.post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    if request.method == 'POST':
        comment.delete()
        return redirect('post_details', pk=post_pk)

    return render(request, 'social/comment_delete_confirm.html', {'comment': comment})