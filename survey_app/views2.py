# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index2(request):
    return HttpResponse("Hello, world.")
    #return render(request, 'login.html')



def index(request):
    if request.user.is_authenticated:
        # Redirect to a success page or dashboard page
        full_uri = request.session.get('full_uri', None)
        if full_uri is None:
            return redirect('success')
        else:
            del request.session['full_uri']  # Clear the session variable after using it
            return redirect(full_uri)
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        print("Hello")
        request.session['full_uri'] = request.build_absolute_uri("/surveys/")
        print(request.session['full_uri'])
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')
