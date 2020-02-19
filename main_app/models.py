from django.db import models

# Create your models here.
class Experience(models.Model):
  title = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Booked(models.Model):
  experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='experiences')
  
  def __str__(self):
    return self.title