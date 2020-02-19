from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control', 'cols':'80'})

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 's_content', 'content', 'slug', 'category', 'status')

class CatForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('title', 'content', 'slug', 'status', )