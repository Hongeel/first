from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', include('weatherapp.urls')),
    path('cookbook/', include('cookbook.urls')),
]