from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from posts.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='posts')
router.register(prefix='posts/(?P<post_id>\d+)/comments',
                viewset=CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]

urlpatterns += [
    path('v1/api-token-auth/', views.obtain_auth_token)
]
