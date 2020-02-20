from django import forms
from .models import Adventure, Booking

# class DateInput(forms.DateInput):
#     input_type = 'date'

class AdventureForm(forms.ModelForm):
    class Meta:
        # my_date_field = forms.DateField()
        model = Adventure
        fields = [
            'creator',
            'title',
            'description',
            'price',
            'picture',
            'location',
            'date'
        ]

class AdventureFormNew(forms.Form):
    creator = forms.CharField()
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={"placeholder":"Title"}
        )
    )
    description = forms.CharField()
    price = forms.DecimalField(label='')
    picture = forms.CharField()
    location = forms.CharField(label='')
    date = forms.DateField()

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ()
