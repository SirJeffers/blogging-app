from django.urls import path

from . import views

#the url patterns are for showing the homepage, creating a post, viewing a post
#editing the post, viewing the authors info, but not creating one as this would be done by an admin
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createPost, name='Create'),
    path('<int:post_id>/post/', views.postview, name='Post'),
    path('<int:post_id>/edit/', views.editPost, name='Edit'),
    path('<int:auth_id>/author/', views.authInfo, name='Author'),
]