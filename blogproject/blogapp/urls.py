from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createPost, name='Create'),
    path('<int:post_id>/post/', views.postview, name='Post'),
    path('<int:post_id>/edit/', views.editPost, name='Edit'),
]