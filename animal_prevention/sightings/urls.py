from django.urls import path
from .views import home, sighting_list

urlpatterns = [
    path('', home, name='home'),
    path('sighting/list/', sighting_list, name='sighting_list'),
]
