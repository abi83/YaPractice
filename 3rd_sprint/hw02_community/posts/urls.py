from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_list, name='posts-list'),
    path('group/', views.groups_list, name='groups-list'),
    path('group/<slug:slug>/', views.group_posts, name='group-posts'),
]