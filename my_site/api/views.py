from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializers
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset= BlogPost.objects.all()
    serializer_class= BlogPostSerializers

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= BlogPost.objects.all()
    serializer_class= BlogPostSerializers
    lookup_field= "pk"


def login_view(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        user= authenticate(request, username, password)
        
        if user is not None:
            login(request, user)
            redirect('')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'api/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')                       

def register_view(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]
        confirm_password= request.POST["confirm_password"]

        if password== confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exists.')
            else:
                user= User.objects.create(username, password)
                login(request,user)
                redirect('')    
        else: 
            messages.error(request,'Password does not not match')
    
    return render(request, 'api/register.html')