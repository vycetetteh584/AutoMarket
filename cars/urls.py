from django.urls import path, include
from .views import car_list
from .views import car_detail

urlpatterns = [
    path("", car_list, name = "car-list"),
    path("<int:pk>/",car_detail, name = "car_list")
    ]
