from django.shortcuts import get_object_or_404, render
from .models import Blog, Category,Tags
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def home(request):
    blogs=Blog.objects.order_by('-created_date')
    context={
        "blogs":blogs
    }
    return render(request, 'home.html',context)

def blogs(request):
    queryset=Blog.objects.order_by('-created_date')
    paginator=Paginator(queryset,2)
    page=request.GET.get('page',1)
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs=paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    
    context={
        "blogs":blogs,
        "paginator":paginator,
    }
    return render(request,'blog.html',context)


def Category_blogs(request,slug):
    categoty=get_object_or_404(Category,slug=slug)
    queryset=categoty.category_blogs.all()
    paginator=Paginator(queryset,2)
    page=request.GET.get('page',1)
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs=paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    context={
        "blogs":blogs,
        
    }
    return render(request,'category_blogs.html',context)

def Tag_blogs(request,slug):
    tag=get_object_or_404(Tags,slug=slug)
    queryset=tag.tag_blogs.all()
    paginator=Paginator(queryset,2)
    page=request.GET.get('page',1)
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs=paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    context={
        "blogs":blogs,
        
    }
    return render(request,'tag_blogs.html',context)

def blog_details(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    category=Category.objects.get(id=blog.category.id)
    related_blogs=category.category_blogs.all()
    context={
        "blog":blog,
        "related_blogs":related_blogs
    }

    return render(request,'blog_details.html',context)