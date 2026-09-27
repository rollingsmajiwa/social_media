from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm
from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer


# 1. HTML TEMPLATE VIEWS


def post_lists(request):
    posts = Post.objects.all().order_by('-created_on')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            if request.user.is_authenticated:
                new_post.author = request.user
            new_post.save()
            return redirect('post_lists')
    else:
        form = PostForm()

    return render(request, 'social/post.html', {'posts': posts, 'form': form})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
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

    return render(request, 'social/post_details.html', {'post': post, 'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'social/post_edit.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_lists')

    return render(request, 'social/post_delete.html', {'post': post})


# 2. REST FRAMEWORK API VIEWS


@api_view(['GET', 'POST'])
def api_post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def api_comment_list(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def api_comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_profile_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Ensure a user can only update their own profile
        if request.user != user:
            return Response(
                {'detail': 'You do not have permission to edit this profile.'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # partial=True allows updating specific fields without requiring all fields
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # REST API Profile Detail View
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def api_profile_detail(request, user_id):
    user_obj = get_object_or_404(User, pk=user_id)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user_obj, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user != user_obj:
            return Response({'detail': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = UserProfileSerializer(user_obj, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# HTML Profile Template View

def profile_view(request, user_id):
    user_obj = get_object_or_404(User, pk=user_id)
    # Ensure profile exists for existing users
    Profile.objects.get_or_create(user=user_obj)
    return render(request, 'social/profile.html', {'profile_user': user_obj})

# edit prifile view
@login_required
def edit_profile_view(request, user_id):
    if request.user.id != user_id:
        return redirect('profile_view', user_id=request.user.id)

    # Safely retrieve or create the Profile object for the current user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile_view', user_id=request.user.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'social/edit_profile.html', context)