from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('blogs/',blogs,name='blogs'),
    path('category_blogs/<str:slug>',Category_blogs,name='category_blogs'),
    path('tag_blogs/<str:slug>',Tag_blogs,name='tag_blogs'),
    path('blog_details/<str:slug>',blog_details,name='blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>/',add_reply,name='add_reply'),
]
