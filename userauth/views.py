from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

# Create your views here.

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            messages.info(request, 'Invalid Info')
            return render(request, 'auth/login.html')

    else:
        return render(request, 'auth/login.html') 

def logoutUser(request):
    logout(request)
    return redirect("/userauth/login") 

def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect("/signup")

        form = User.objects.create_user(username, email)
        form.set_password(password)
        form.save()

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")

    return render(request, 'auth/signup.html')
