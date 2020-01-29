from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("lk/", include("authentication.urls")),  # add this
    path("lk/", include("app.urls")),  # add this
    path('weather/', include('weatherapp.urls')),
    path('cookbook/', include('cookbook.urls')),
]