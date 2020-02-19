from django import forms
from .models import Adventure, Booking

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('creator', 'title', 'description', 'price', 'picture', 'location', 'date')