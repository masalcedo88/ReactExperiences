from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Adventure, Booking
from .forms import AdventureForm, BookingForm

# Create your views here.


def index(request):
  # adventures = Adventure.objects.exclude(id__in=Booking.objects.filter(adventure=None))
  adventures = Adventure.objects.all()
  return render(request, 'index.html', {'adventures': adventures})

def adventure_detail(request, pk):
  adventure = Adventure.objects.get(id=pk)
  return render(request, 'adventure_detail.html', {'adventure': adventure})

@login_required
def profile(request):
  return render(request, 'profile.html')

@login_required
def adventure_create(request):
    if request.method == 'POST':
      form = AdventureForm(request.POST)
      if form.is_valid():
        adventure = form.save(commit=False)
        adventure.creator = request.user
        adventure.save()
        return redirect('profile')
    else:
      form = AdventureForm()
    context = {'form': form, 'header': "Add New Adventure"}
    return render(request, 'adventure_form.html', context)

@login_required
def adventures_list(request):
  return render(request, 'my_adventures.html')

@login_required
def book_adventure(request, pk):
  customer = request.user
  adventure = Adventure.objects.get(pk=pk)
  booking = Booking.objects.create(customer=customer, adventure=adventure)
  return redirect('profile')