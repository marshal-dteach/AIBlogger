from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from blog.forms import CommentForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.models import Post, Comment
from blog_poster import create_blog_post
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
import re

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post,
            
                    )
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
            "post": post,
            "comments": comments,
            "form": CommentForm(),
            }
    return render(request, "blog/post_detail.html", context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def is_admin(user):
    return user.is_authenticated and user.is_staff    

@user_passes_test(is_admin)
def createAIpost(request):
        try:
            #process data here
            user_AI = 'traveller'
            hobbies_AI = ["travelling to a certain random place", "exploring new places", "riding motorcycles"]
            post_AI = create_blog_post(user_AI, hobbies_AI)

            #pattern = re.compile(r'(\w+): (.+)')
            string_data = post_AI.replace('\n', '').replace('\r', '')
            #matches = pattern.findall(post_AI)
            #data_filter = dict(post_AI)
            json_data = json.loads(string_data)

            #username object fetching
            user_instance = get_user_model().objects.get(username=user_AI)
            post = Post(title=json_data['title'], context=json_data['context'], author=user_instance)
            print(json_data)
            post.save()         

            return JsonResponse(json_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Invalid JSON data: {str(e)}'}, status=400)
        


