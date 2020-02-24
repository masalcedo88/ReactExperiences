from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  picture_url = models.TextField()
  picture = models.ImageField(upload_to='user_image', default='default.jpg')
  interests = models.TextField(null=True)

  def __str__(self):
    return self.user.username