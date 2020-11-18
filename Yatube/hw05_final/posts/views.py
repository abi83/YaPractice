from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import PostForm, CommentForm
from .models import Post, Group, Follow


class PostCreate(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        form = PostForm()
        return render(request, 'posts/new_post.html', {
            'form': form,
        })

    @staticmethod
    def post(request):
        form = PostForm(request.POST, files=request.FILES or None)
        if not form.is_valid():
            return render(request, 'posts/new_post.html', {'form': form})
        form.instance.author = request.user
        form.save()
        return redirect('posts')


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/new_post.html'
    pk_url_kwarg = 'post_id'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('post', args=[
            self.get_object().author.username,
            self.get_object().pk])
        if request.user != self.get_object().author:
            return redirect(self.success_url)
        super(UpdateView, self).post(request, *args, **kwargs)
        return redirect(self.success_url)


class PostView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['author'] = self.object.author
        context['show_form'] = False
        context['form'] = CommentForm()
        return context


class PostAddComment(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username: str, post_id: int):
        post_author = get_object_or_404(User, username=username)
        post = get_object_or_404(
            Post,
            pk=post_id,
            author=post_author, )
        form = CommentForm()
        return render(request, 'posts/post.html', {
            'post': post,
            'form': form,
            'show_form': True,
        })

    @staticmethod
    def post(request, username: str, post_id: int):
        post_author = User.objects.get(username=username)
        post = get_object_or_404(
            Post,
            pk=post_id,
            author=post_author, )
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect('post', username=username, post_id=post_id)
        return render(request, 'posts/post.html', {
            'post': post,
            'form': form,
        })


class ProfilePosts(View):
    @staticmethod
    def get(request, username: str):
        author = get_object_or_404(User, username=username)
        posts = author.posts.filter(active=True,)
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
        following = request.user.is_authenticated \
            and Follow.objects.filter(user=request.user,
                                      author__username=username
                                      ).exists()
        return render(request, 'posts/profile.html', {
            'author': author,
            'posts': posts,
            'paginator': paginator,
            'page': paginator.page(page_number),
            'following': following,
        })


class ProfileFollow(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username: str):
        author = get_object_or_404(User, username=username)
        if request.user.is_authenticated and author != request.user:
            Follow.objects.get_or_create(author=author, user=request.user)
        return redirect('profile', username=username)


class ProfileUnFollow(LoginRequiredMixin, View):
    @staticmethod
    def get(request, username: str):
        author = get_object_or_404(User, username=username)
        if request.user.is_authenticated:
            Follow.objects.get(author=author, user=request.user
                               ).delete()
        return redirect('profile', username=username)


class GroupPosts(View):
    @staticmethod
    def get(request, slug: str):
        group = get_object_or_404(Group, slug=slug, active=True)
        posts = group.posts.filter(active=True, )
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
    query_set = Group.objects.filter(active=True, )
    qs_name = 'groups'
    template = 'posts/groups_list.html'


class ProfilesList(ItemsListMixin, View):
    query_set = User.objects.exclude(posts=None, )
    qs_name = 'users'
    template = 'posts/profiles_list.html'


@method_decorator(cache_page(20, key_prefix='index_page'), name='dispatch')
class IndexList(ItemsListMixin, View):
    query_set = Post.objects.filter(active=True,
                                    ).select_related('author', 'group')
    qs_name = 'posts'
    template = 'posts/index.html'


class FollowList(LoginRequiredMixin, ItemsListMixin, View):
    def dispatch(self, request, *args, **kwargs):
        following = Follow.objects.filter(
            user__id=request.user.id
        ).select_related('author')
        self.query_set = Post.objects.filter(
            author__in=[f.author for f in following]
        )
        return super(FollowList, self).dispatch(request, *args, **kwargs)

    qs_name = 'posts'
    template = 'posts/follow.html'


class Handler404(View):
    @staticmethod
    def get(request, exception):  # noqa
        return render(request, 'misc/404.html',
                      {'path': request.path}, status=404)


class Handler500(View):
    @staticmethod
    def dispatch(request, *args, **kwargs):
        return render(request, 'misc/500.html', status=500)
