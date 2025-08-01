from urllib import request
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category, Reply,Tags,Comment,User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import TextForm,AddBlogForm
from django.db.models import Q

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
    form=TextForm()
    blog=get_object_or_404(Blog,slug=slug)
    category=Category.objects.get(id=blog.category.id)
    related_blogs=category.category_blogs.all()

    if request.method == "POST" and request.user.is_authenticated:
     form=TextForm(request.POST)
     if form.is_valid():
         Comment.objects.create(
             user=request.user,
             blog=blog,
             text=form.cleaned_data.get('text'),
         )
         return redirect('blog_details',slug=slug)

    context={
        "blog":blog,
        "related_blogs":related_blogs,
        "form":form
    }

    return render(request,'blog_details.html',context)

@login_required(login_url='login')
def add_reply(request,blog_id,comment_id):
    
    if request.method == "POST":
        form=TextForm(request.POST)
        if form.is_valid():
            blog=get_object_or_404(Blog,id=blog_id)
            comment=get_object_or_404(Comment,id=comment_id)
            Reply.objects.create(
        user=request.user,
        comment=comment,
        text=form.cleaned_data.get('text')
    )
    return redirect('blog_details', slug=blog.slug)
    
    
def search_blogs(request):

    search_key=request.GET.get('search',None)
    if search_key:
        blogs=Blog.objects.filter(
            Q(title__icontains=search_key)|
            Q(category__title__icontains=search_key)|
            Q(user__username__icontains=search_key)|
            Q(tags__title__icontains=search_key)
        ).distinct()

        context={
            "blogs":blogs,
            "search_key":search_key,
        }

        return render(request,'search.html',context)
    else:
        blogs=Blog.objects.order_by('-created_date')
        context={
            "blogs":blogs,
        }
        return render(request,'search.html',context)

@login_required(login_url='login')
def my_blogs(request):
    queryset=request.user.user_blogs.all()

    paginator=Paginator(queryset,3)
    page=request.GET.get('page',1)
    delete=request.GET.get('delete',None)

    if delete:
        blog=get_object_or_404(Blog, pk=delete)

        if request.user.pk!=blog.user.pk:
            return redirect('home')
        

        blog.delete()
        return redirect('my_blogs')
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs=paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    context={
        "blogs":blogs,
        "paginator":paginator
        
    }
    return render(request, 'my_blogs.html',context)

@login_required(login_url='login')
def add_blog(request):
    form=AddBlogForm()

    if request.method == "POST":
        form=AddBlogForm(request.POST,request.FILES)

        if form.is_valid():
            tags = request.POST['tags'].split(',')
            user=get_object_or_404(User,pk=request.user.pk)
            category=get_object_or_404(Category,pk=request.POST['category'])
            blog=form.save(commit=False)
            blog.user=user
            blog.category=category
            blog.save()

            for tag in tags:
                tag_input = Tag.objects.filter(
                    title__iexact=tag.strip(),
                    slug=slugify(tag.strip())
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)

                else:
                    if tag != '':
                        new_tag = Tags.objects.create(
                            title=tag.strip(),
                            slug=slugify(tag.strip())
                        )
                        blog.tags.add(new_tag)

            
            return redirect('blog_details', slug=blog.slug)
        else:
            print(form.errors)
    context={
        "form":form,
    }
    return render(request,'add_blog.html',context)

@login_required(login_url='login')
def update_blog(request,slug):
    
    blogs=get_object_or_404(Blog,slug=slug)
    form=AddBlogForm(instance=blogs)

    if request.method == "POST":
        form=AddBlogForm(request.POST,request.FILES,instance=blogs)

        if form.is_valid():

            if request.user.pk!=blog.user.pk:
                return redirect('home')
            tags = request.POST['tags'].split(',')
            user=get_object_or_404(User,pk=request.user.pk)
            category=get_object_or_404(Category,pk=request.POST['category'])
            blog=form.save(commit=False)
            blog.user=user
            blog.category=category
            blog.save()

            for tag in tags:
                tag_input = Tags.objects.filter(
                    title__iexact=tag.strip(),
                    slug=slugify(tag.strip())
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)

                else:
                    if tag != '':
                        new_tag = Tag.objects.create(
                            title=tag.strip(),
                            slug=slugify(tag.strip())
                        )
                        blog.tags.add(new_tag)

            
            return redirect('blog_details', slug=blog.slug)
        else:
            print(form.errors)
    context={
        "form":form,
        "blogs":blogs,
    }
    return render(request,'update_blog.html',context)