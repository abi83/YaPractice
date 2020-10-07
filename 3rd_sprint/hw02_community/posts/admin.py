from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    empty_value_display = '-пусто-'
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'active')
    search_fields = ('title', 'description')