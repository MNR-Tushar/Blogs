from .models import *

def get_all_categories(request):

    category=Category.objects.all()

    context={
        "categories":category
    }
    return context

def get_all_tags(request):
    tag=Tags.objects.all()

    context={
        "tags":tag
    }

    return context