from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.posts_list,
         name='posts'),
    path('post/<int:post_id>/',
         views.post_detail,
         name='post-detail'),
    path('group/',
         views.groups_list,
         name='groups'),
    path('group/<slug:slug>/',
         views.group_detail,
         name='group-posts'),
    path('new/',
         views.new_post,
         name='new-post'),
]
