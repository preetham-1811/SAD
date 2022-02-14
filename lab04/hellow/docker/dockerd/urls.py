from django.urls import path
from dockerd import views


urlpatterns = [
    path('', views.dockerd, name='dockerd' ),
]
