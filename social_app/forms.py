from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from .models import Profile

class PostForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-gray-800 text-gray-100 rounded-lg p-3 border border-gray-700 placeholder-gray-400',
            'rows': 3,
            'placeholder': "What's on your mind?",
        }),
        label=''
    )

    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-gray-800 text-gray-100 rounded-lg p-3 border border-gray-700 placeholder-gray-400',
            'rows': 3,
            'placeholder': "What\'s on your mind?",
        }),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['comment']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']