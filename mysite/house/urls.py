from django.urls import path
from . import views

urlpatterns = [
    path('house/', views.house, name='house'),
]

