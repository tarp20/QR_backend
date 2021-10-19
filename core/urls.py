from django.urls import path, include

from . import views

urlpatterns = [
    path('places/', views.PlaceList.as_view())
]
