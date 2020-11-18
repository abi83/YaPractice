from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView

from .form import PostForm
from .models import Post, Group


class PostCreate(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    @staticmethod
    def get(request):
        form = PostForm()
        return render(request, 'posts/new_post.html', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = PostForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/new_post.html', {'form': form})
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts')


class PostEdit(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username: str, post_id: int):
        author = get_object_or_404(User, username=username)
        post = get_object_or_404(
            Post,
            pk=post_id,
            author=author,
        )
        if request.user != author:
            return redirect('post', username=username, post_id=post_id)
        form = PostForm(instance=post)
        return render(request, 'posts/new_post.html', {
            'post': post,
            'form': form,
        })

    @staticmethod
    def post(request, username: str, post_id: int):
        author = User.objects.get(username=username)
        post = get_object_or_404(
            Post,
            pk=post_id,
            author=author,
        )
        if request.user != author:
            return redirect('post', username=username, post_id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid() and author == request.user:
            form.save()
            return redirect('post', username=username, post_id=post_id)
        return render(request, 'posts/new_post.html', {
            'post': post,
            'form': form,
        })


class PostView(View):
    @staticmethod
    def get(request, username: str, post_id: int):
        author = get_object_or_404(User, username=username)
        post = get_object_or_404(
            Post,
            pk=post_id,
            author=author,
            active=True,
        )
        return render(request, 'posts/post.html', {
            'post': post,
            'author': author,
        })


class ProfilePosts(View):
    @staticmethod
    def get(request, username: str):
        author = get_object_or_404(User, username=username)
        posts = author.posts.filter(
            active=True,
        )
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'posts/profile.html', {
            'author': author,
            'posts': posts,
            'paginator': paginator,
            'page': paginator.page(page_number),
        })


class GroupPosts(View):
    @staticmethod
    def get(request, slug: str):
        group = get_object_or_404(Group, slug=slug)
        posts = group.posts.filter(
            active=True,
        )
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        return render(request, 'group.html', {
            'group': group,
            'posts': posts,
            'paginator': paginator,
            'page': paginator.page(page_number),
        })


class ItemsListMixin:
    query_set = None
    qs_name: str = None
    template: str = None

    def get(self, request):
        """
        Make paginated context dictionary for the list of items self.query_set
        and calling render function for it with self.template
        """
        paginator = Paginator(self.query_set, 10)
        page_number = request.GET.get('page', 1)
        paginated_qs = paginator.get_page(page_number)
        return render(request, self.template, {
            self.qs_name: paginated_qs,
            'paginator': paginator,
            'page': paginator.page(page_number if page_number else 1),
        })


class GroupsList(ItemsListMixin, View):
    query_set = Group.objects.filter(
        active=True,
    )
    qs_name = 'groups'
    template = 'posts/groups_list.html'


class ProfilesList(ItemsListMixin, View):
    query_set = User.objects.exclude(
        posts=None,
    )
    qs_name = 'users'
    template = 'posts/profiles_list.html'


class PostsList(ItemsListMixin, View):
    query_set = Post.objects.filter(
        active=True,
    )
    qs_name = 'posts'
    template = 'posts/index.html'


class Handler404(View):
    @staticmethod
    def get(request, exception):
        return render(request, 'misc/404.html',
                      {'path': request.path}, status=404)


# class Handler500(TemplateView):
#     template_name = 'misc/500.html'
#     @classmethod
#     def as_error_view(cls):
#         v = cls.as_view()
#         def view(request):
#             r = v(request)
#             r.render()
#             return r
#         return view

class Handler500(View):
    @staticmethod
    def dispatch(request, *args, **kwargs):
        return render(request, 'misc/500.html', status=500)