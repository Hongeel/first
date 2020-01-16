"""myapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework import routers
from mainsite import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Category', views.CategoryViewSet)

from login import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('api', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)