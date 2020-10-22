from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .form import PostForm
from .models import Post, Group


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)


def posts_list(request):
    posts = Post.objects.filter(
        active__exact=True,
    )
    return render(request, 'index.html', {'posts': posts})


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'new_post.html', {'form': form})
    post = form.save(commit=False)
    post.author = request.user
    post.save()
    return redirect('posts')


def groups_list(request):
    groups = Group.objects.filter(
        active__exact=True,
    )
    context = {
        'groups': groups,
    }
    return render(request, 'group_list.html', context)


def group_detail(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.filter(
        active__exact=True,
    )
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, 'group.html', context)

