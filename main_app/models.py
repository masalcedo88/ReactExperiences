from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Experience(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experiences")
  title = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  picture = models.TextField()
  location = models.CharField(max_length=250)
  date = models.DateField()

  def __str__(self):
    return self.title

# identical related names mean that you can select experience.booked to return all booked experiences or user.booked to return all bookings made by a particular user
# autopopulate arguments for date_booked aren't working, need to consult Dalton. 
class Booked(models.Model):
  experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="booked")
  customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked")
  date_booked = models.DateField()
  confirmed = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title