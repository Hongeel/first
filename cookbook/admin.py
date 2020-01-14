from django.contrib import admin
from .models import Post, Comment, Category
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'category','created_on')
    list_filter = ("status", 'category')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryPost(admin.ModelAdmin):
    list_display = ('title','created_at','slug', 'status',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)