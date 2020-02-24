from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Adventure(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adventures")
  title = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=8, decimal_places=2)
  picture = models.ImageField(upload_to='adventure_image', default='default.jpg')
  location = models.CharField(max_length=250)
  date = models.DateField()

  def __str__(self):
    return self.title

# identical related names mean that you can select adventure.bookings to return all booked adventures or user.bookings to return all bookings made by a particular user
# autopopulate arguments for date_booked aren't working, need to consult Dalton. 

class Booking(models.Model):
  adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="bookings")
  customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
  date_booked = models.DateField(auto_now_add=True)
  confirmed = models.BooleanField(default=False)
  
  def __str__(self):
    return self.adventure.title