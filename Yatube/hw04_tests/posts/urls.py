from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.PostsList.as_view(),
         name='posts'),
    path('group/',
         views.GroupsList.as_view(),
         name='groups'),
    path('group/<slug:slug>/',
         views.GroupPosts.as_view(),
         name='group-posts'),
    path('authors/',
         views.ProfilesList.as_view(),
         name='authors'),
    path('new/',
         views.PostCreate.as_view(),
         name='new-post'),
    path('<str:username>/',
         views.ProfilePosts.as_view(),
         name='profile'),
    path('<str:username>/<int:post_id>/',
         views.PostView.as_view(),
         name='post'),
    path('<str:username>/<int:post_id>/edit/',
         views.PostEdit.as_view(),
         name='post_edit'),
]
