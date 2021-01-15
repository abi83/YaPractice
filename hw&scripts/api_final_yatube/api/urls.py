from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import *

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='posts')
router.register(prefix=r'posts/(?P<post_id>\d)/comments',
                viewset=CommentViewSet, basename='comments')
router.register(prefix='group', viewset=GroupViewSet, basename='group')
router.register(prefix='follow', viewset=FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
]

urlpatterns += [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
