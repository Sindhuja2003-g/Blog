from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('trip/',trip,name="trip"),
    path('height/',height,name="height"),
    path('cooking/',cooking,name="cooking"),
    path('dogs/',dogs,name="dogs"),
    path('kitchen/',kitchen,name="kitchen"),
]
