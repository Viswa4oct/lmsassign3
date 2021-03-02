from django.urls import path
from .views import coursedetails

urlpatterns = [
    path('coursedetails/', coursedetails)
]
