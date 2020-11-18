from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views
from django.conf.urls import handler404, handler500
from posts.views import Handler404, Handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('about/', include('django.contrib.flatpages.urls')),
]
# main flatpages
urlpatterns += [
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
    path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about-author'),
    path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='spec'),
]
# posts app
urlpatterns += [
    path('', include('posts.urls')),
]

urlpatterns += [
    path('', include('posts.urls')),
]

handler404 = Handler404.as_view() # noqa
handler500 = Handler500.as_view() # noqa
