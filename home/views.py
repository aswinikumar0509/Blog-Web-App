from django.shortcuts import render,HttpResponse
from .models import Contacts
from blog.models import Post

# Create your views here.

def home(request):
    return render(request,"home/home.html")

def about(request):
    return render(request,"home/about.html")

def contact(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        contact = Contacts(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,"home/contact.html")



def search(request):
    query = request.GET['query']
    allposts = Post.objects.filter(title__icontains=query)
    output = {'allposts':allposts}
    return render(request,'home/search.html',output)