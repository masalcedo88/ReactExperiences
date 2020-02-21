from django import forms
from PIL import Image

class UserForm(forms.ModelForm):
  picture = forms.ImageField(required=False)
  class Meta:
    model = User
    fields = [
      'first_name',
      'last_name',
      'email',
      'picture'
    ]