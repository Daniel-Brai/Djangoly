from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# class BlogListView(ListView):
#     model = Post
#     template_name = 'blog/post/post_list.html'

# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post/post_detail.html'

def post_list(request):
    posts = Post.published.all()
    return render(request,
            'blog/post/post_list.html',
            {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                                    id=id,
                                    status=Post.Status.PUBLISHED)
    return render(request,
                'blog/post/post_detail.html',
                {'post': post})