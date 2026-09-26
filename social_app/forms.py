from django import forms
from .models import Post

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