from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.

def blogPage(request):
    allposts = Post.objects.all()
    content = {"allposts":allposts}
    return render(request,'blog/blogpage.html',content)


def blogPost(request,slug):
    post = Post.objects.filter(slug=slug)
    context = {'post':post}
    return render(request,'blog/blogpost.html',context)

