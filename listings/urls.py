from django.urls import path
from .views import lists, listing, search

urlpatterns = [
    path('', lists, name='listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search/', search, name='search'),
]
