from django.shortcuts import render, get_object_or_404

from .models import Post, Group

def posts_list(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request, 'index.html', {'posts': latest})

def groups_list(request):
    ten_groups = Group.objects.all()[:10]
    return render(request, 'group_list.html', {'groups': ten_groups})

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group_posts = Post.objects.filter(group_id=group.pk).order_by('-pub_date')[:12]
    context = {
        'posts': group_posts,
        'group': group,
    }
    return render(request, 'group.html', context)