from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileUpdateForm
from .models import Profile


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
          profile = Profile.objects.create(user=user)
          return redirect('/')
    else:
      context = {'error':'Passwords do not match'}
      return render(request, 'signup.html', context)
  else:
    return render(request, 'signup.html')

@login_required
def edit_info(request):
  user = request.user
  form = UserForm(instance=user)
  profile = ProfileUpdateForm(instance=user.profile)
  
  if request.method == "POST":
    form = UserForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
      print('Saving USER update')
      form.save()
    profile = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
    if profile.is_valid():
      print('Saving PROFILE update')
      profile.save()
      return redirect('profile')
  
  context = {'form':form, 'profile':profile}
  # else:
  return render(request, 'edit_info.html', context)

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

def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Your password was successfully updated!')
      return redirect('profile')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'change_password.html', {
    'form': form
  })

def logout(request):
  auth.logout(request)
  return redirect('index')

# def profile(request)