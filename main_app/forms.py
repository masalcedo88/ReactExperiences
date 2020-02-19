from django import forms
from .models import Adventure, Booking

class AdventureForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('title', 'description', 'price', 'picture', 'location', 'date')