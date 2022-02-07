from . import views
from django.urls import path

app_name = 'pure_html'

urlpatterns =[

    path('pure_html/', views.index, name = 'index')
]