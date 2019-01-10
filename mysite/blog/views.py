from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     '''Test Books are active by default'''
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 每页3篇文章
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # 若页码不为数字返回首页
#         posts = paginator.page(1)
#     except EmptyPage:
#         # 若页码超出范围返回最后一页
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                     'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})