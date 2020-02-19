from django.urls import path, include
from .views import post_new, post_detail, PostList, post_edit, CategoryList, SearchResultsView, PostCatList, cat_new


urlpatterns = [
    path('', PostList.as_view(), name='cook'),
    path('new/', post_new, name='post_new'),
    path('catnew/', cat_new, name='cat_new'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/', PostCatList.as_view(), name='PostCatList'),
    path('category/<category>/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<category>/<slug:slug>/edit/', post_edit, name='post_edit'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    
]

    

