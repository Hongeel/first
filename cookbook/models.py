from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 



STATUS = (
    (0,"На модерации"),
    (1,"Опубликован")
)

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, unique=True, verbose_name=('Ссылка'))
    content = RichTextUploadingField(null=True, verbose_name=('Описание'))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=('Статус'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=('Название'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=('Ссылка'))
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', verbose_name=('Автор'))
    s_content = RichTextUploadingField(null=True, max_length=650, verbose_name=('Краткое сожержимое'))
    content = RichTextUploadingField(verbose_name=('Содержимое'))
    updated_on = models.DateTimeField(auto_now= True, verbose_name=('обновлено'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=('Создано'))
    status = models.IntegerField(choices=STATUS, default=0, verbose_name=('Статус'))
    category = models.ForeignKey(Category, null=True, on_delete= models.CASCADE, verbose_name="Категория")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, verbose_name=('Имя'))
    email = models.EmailField()
    body = RichTextField(verbose_name=('Содержимое'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=('Создано'))
    active = models.BooleanField(default=False, verbose_name=('Статус'))

    class Meta:
        ordering = ['created_on']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

