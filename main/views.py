from django.shortcuts import render,redirect
from . forms import RegisterForms, EditProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from blogpost.models import Blog

# Create your views here.

def signup(request):
    form = RegisterForms()
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account created Successfully')
            return redirect('signup')
    context = {'form':form}
    return render(request, 'main/signup.html', context)


def signin(requst):
    if requst.method=='POST':
        email = requst.POST['email']
        password = requst.POST['password']
        
        user = authenticate(requst, email=email, password=password)
        if user is not None:
            login(requst, user)
            return redirect('home')
        else:
            messages.warning(requst, 'Invalid credentials')
            return redirect('signin')
    return render(requst, 'main/login.html')

def signout(requst):
    logout(requst)
    return redirect('home')

def profile(request):
    user = request.user
    blogs = Blog.objects.filter(user=user)
    return render(request, 'main/profile.html',{'user':user,'blogs':blogs})

@login_required(login_url='signin')
def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form =EditProfile(instance=user)
        if request.method=="POST":
            form = EditProfile(request.POST, request.FILES,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updateded Successfuly')
                return redirect('profile')
    return render(request, 'main/edit_profile.html',{'form':form})





def users(request):
    return render(request, 'main/users.html')