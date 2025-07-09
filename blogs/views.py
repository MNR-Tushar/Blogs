from django.shortcuts import render
from .models import Blog
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