from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    UserPostListView
)

from . import views
urlpatterns = [
    path('',PostListView.as_view(), name="blog-home" ),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('about/',views.about, name="blog-about" ),
    path('spawn/', views.createAIpost, name='createAIpost')
]
