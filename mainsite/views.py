from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CategorySerializer
from cookbook.models import Category
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator 
from django.views.generic import TemplateView


def index(request):
    

    return render(request, 'mainsite/index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    template_name = 'login.html'
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    @method_decorator(login_required(login_url='/api-auth/login/'))
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    @method_decorator(login_required(login_url='/api-auth/login/'))
    def dispatch(self, *args, **kwargs):
        return super(GroupViewSet, self).dispatch(*args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @method_decorator(login_required(login_url='/api-auth/login/'))
    def dispatch(self, *args, **kwargs):
        return super(CategoryViewSet, self).dispatch(*args, **kwargs)