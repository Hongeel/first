from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 's_content', 'content', 'slug', 'category', 'status', )

class CatForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('title', 'content', 'slug', 'status', )