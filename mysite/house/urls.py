from django.urls import path
from . import views

app_name = 'house'
urlpatterns = [
    path('', views.house, name='house'),
    path('<int:activity_id>/', views.detail, name='detail'),
  
    path('<int:activity_id>/about/', views.about, name='about'),
   
    path('<int:activity_id>/category/', views.category, name='category'),
]
