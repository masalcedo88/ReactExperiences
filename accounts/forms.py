from django import forms
from PIL import Image
from .models import User, Profile

class UserForm(forms.ModelForm):
  picture = forms.ImageField(required=False)
  class Meta:
    model = User
    fields = [
      'first_name',
      'last_name',
      'email',
      'picture',
      # 'interests'
    ]

# WORKING HERE
# class ProfileUpdateForm(forms.ModelForm):
#   # user = models.OneToOneField(User, on_delete=models.CASCADE)
#   # picture = models.ImageField(default='default.jpg', upload_to='user_image')
#   class Meta:
#     model = Profile
#     fields = [
#       'picture',
#       # 'interests'
#     ]
# WORKING HERE