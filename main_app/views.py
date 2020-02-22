from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Adventure, Booking
from .forms import AdventureForm, BookingForm

# Create your views here.

def index(request):
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
    form = AdventureForm(request.POST, request.FILES)
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
  bookings = Booking.objects.filter(customer=request.user)
  return render(request, 'my_adventures.html', {'bookings': bookings})

@login_required
def adventures_offered(request):
  adventures = Adventure.objects.all()
  return render(request, 'adventures_offered.html', {'adventures': adventures})

@login_required
def book_adventure(request, pk):
  customer = request.user
  adventure = Adventure.objects.get(pk=pk)
  booking = Booking.objects.create(customer=customer, adventure=adventure)
  return redirect('adventures_list')

@login_required
def confirm_booking(request, pk):
  booking = Booking.objects.get(pk=pk)
  booking.confirmed = True
  booking.save()
  return redirect('adventures_list')

@login_required
def cancel_booking(request, pk):
  Booking.objects.get(id=pk).delete()
  return redirect('adventures_list')

@login_required
def delete_post(request, pk):
  Adventure.objects.get(id=pk).delete()
  return redirect('adventures_list')