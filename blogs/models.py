from django.db import models
from user_profile.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    title=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(null=True,blank=True)
    created_data=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

class Tags(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(null=True,blank=True)
    created_data=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

class Blog(models.Model):
    user=models.ForeignKey(User,related_name='user_blogs', on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='category_blogs',on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tags,related_name='tag_blogs',blank=True)
    like=models.ManyToManyField(User,related_name='user_like',blank=True)
    title=models.CharField(max_length=250)
    slug=models.SlugField(null=True,blank=True)
    banner=models.ImageField(upload_to='blog_banners')
    description=RichTextField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

class Comment(models.Model):
    user=models.ForeignKey(User,related_name="user_comment",on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,related_name='blog_comment',on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Reply(models.Model):
    user=models.ForeignKey(User,related_name="user_reply",on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,related_name='reply_comment',on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text