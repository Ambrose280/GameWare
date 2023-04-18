from django.shortcuts import render,redirect
from . models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def signup(request):
    if request.method=="POST":
        data = request.POST
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.filter(username=username, email=email)
        if len (user) > 0:
            return render(request, 'signin.html', {'error':'username already exists'})
        else:
            new_user = User.objects.create(username=username, password=password, email=email)
            new_user.save()
            return redirect('signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        email = data['email']
        user = User.objects.filter(username=username, email=email)
        if len (user) > 0:
            pswd = user.values()[0]["password"]  
            if pswd == password:
                request.session["username"] = username
                return redirect("products")
            else:
                return render(request, 'signin.html', {"error": "wrong password"})
    return render(request, 'signin.html')
            

def home(request):
    return render(request, 'homepage.html')
