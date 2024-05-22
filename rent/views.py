from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import HomeRental
from .forms import HomeRentalForm

class HomeRentalListView(ListView):
    model = HomeRental
    template_name = 'homerental_list.html'
    context_object_name = 'rental'

class HomeRentalDetailView(DetailView):
    model = HomeRental
    template_name = 'homerental_detail.html'

class HomeRentalCreateView(CreateView):
    model = HomeRental
    form_class = HomeRentalForm
    template_name = 'createrental_form.html'
    success_url = '/rent/'


