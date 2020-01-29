from django.views import generic
from .models import Post, Category
from .forms import CommentForm, PostForm, CatForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CategoryList(generic.ListView):
    queryset = Category.objects.filter(status=1).order_by('title')
    template_name = 'cookbook/category_list.html'
    paginate_by = 10


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'cookbook/index.html'
    paginate_by = 10

class PostCatList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'cookbook/category_detail.html'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs.get('slug'))
    

def post_detail(request, slug, category):
    template_name = 'cookbook/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    
    # Comment posted
    if request.method == 'POST':
        data = request.POST.copy()
        data.update({'name':request.user.username})
        comment_form = CommentForm(data)
        if comment_form.is_valid():
            comment_form.name = request.user
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm({'name':request.user.username, 'email':request.user.email})
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,})

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'cookbook/post_edit.html', {'form': form})

def cat_new(request):
    
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.published_date = timezone.now()
            category.save()
            return redirect('PostCatList', slug=category.slug)
    else:
        form = CatForm()
    return render(request, 'cookbook/category_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'cookbook/post_edit.html', {'form': form})


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list

