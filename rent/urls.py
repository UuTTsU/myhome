from django.urls import path
from .views import HomeRentalListView, HomeRentalDetailView, HomeRentalCreateView

urlpatterns = [
    path('list/', HomeRentalListView.as_view(), name='homerental_list'),
    path('detail/<int:pk>/', HomeRentalDetailView.as_view(), name='homerental_detail'),
    path('create/', HomeRentalCreateView.as_view(), name='homerental_create'),
]
