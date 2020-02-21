from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username_form = request.POST['username']
    email_form = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
      if User.objects.filter(username=username_form).exists():
        context = {'error': 'Username is already taken.'}
        return render(request, 'signup.html', context)
      else:
        if User.objects.filter(email=email_form).exists():
          context = {'error':'That email already exists.'}
          return render(request, 'signup.html', context)
        else: 
          user = User.objects.create_user(
          username=username_form, 
          email=email_form, 
          password=password, 
          first_name=first_name, 
          last_name=last_name)
        user.save()
        return redirect('/')
    else:
      context = {'error':'Passwords do not match'}
      return render(request, 'signup.html', context)
  else:
    return render(request, 'signup.html')

def edit_info(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    user = User.objects.get(pk=request.user.pk)
    print(user)
    # user.first_name = first_name
    # user.save()
    return redirect('profile')
  else:
    return render(request, 'edit_info.html')

def login(request):
  if request.method == 'POST':
    username_form = request.POST['username']
    password_form = request.POST['password']
    # authenticate user
    user = auth.authenticate(username=username_form, password=password_form)
    if user is not None:
      # login
      auth.login(request, user)
      #redirect
      return redirect('/')
    else:
      context = {'error':'Invalid Credentials'}
      return render(request, 'login.html', context)
  else:
    return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('index')

# def profile(request)