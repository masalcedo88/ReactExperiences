from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdventureForm

# Create your views here.


def index(request):
  return render(request, 'index.html')

@login_required
def profile(request):
  return render(request, 'profile.html')

@login_required
def adventure_create(request):
    if request.method == 'POST':
        form = AdventureForm(request.POST)
        if form.is_valid():
            adventure = form.save()
            return redirect('profile', pk=adventure.pk)
    else:
        form = AdventureForm()
    context = {'form': form, 'header': "Add New Adventure"}
    return render(request, 'adventure_form.html', context)