from django.urls import include, path
from api import views

urlpatterns = [
    path('cars', views.cars_json),
    path('trains', views.trains),
    path('about', views.about),
]
