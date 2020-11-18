from django.contrib import admin

from .models import Post, Group, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'active')
    empty_value_display = '-пусто-'
    search_fields = ('text',)
    list_filter = ('pub_date',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'active')
    list_filter = ('created',)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'user')
    list_filter = ('author', 'user')
