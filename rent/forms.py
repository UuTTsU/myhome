from django import forms
from .models import HomeRental

class HomeRentalForm(forms.ModelForm):
    class Meta:
        model = HomeRental
        fields = ['title', 'address', 'description', 'price', 'available']



