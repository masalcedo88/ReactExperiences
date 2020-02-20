from django import forms
from .models import Adventure, Booking
from PIL import Image

class DateInput(forms.DateInput):
    input_type = 'date'

class AdventureForm(forms.ModelForm):
    class Meta:
        # my_date_field = forms.DateField()
        model = Adventure
        widgets = {
            'date': DateInput(),
            # 'picture': ImageField()
        
        }
        fields = [
            # 'creator',
            'title',
            'description',
            'price',
            'picture',
            'location',
            'date'
        ]

# class AdventureForm(forms.Form):
#     class Meta:
#         widgets = {'date': DateInput()}
    
#     creator = forms.CharField()
#     title = forms.CharField(
#         label='',
#         widget=forms.TextInput(
#             attrs={"placeholder":"Title"}
#         )
#     )
#     description = forms.CharField(
#         label='',
#         widget=forms.TextInput(
#             attrs={"placeholder":"Description"}
#         )
#     )
#     price = forms.DecimalField(
#         label='',
#         widget=forms.TextInput(
#             attrs={"placeholder":"Price"}
#         )
#     )
#     picture = forms.CharField()
#     location = forms.CharField(
#         label='',
#         widget=forms.TextInput(
#             attrs={"placeholder":"Location"}
#         )
#     )
#     date = forms.DateField()

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ()
