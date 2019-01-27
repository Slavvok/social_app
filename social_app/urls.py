from django.urls import path
from . import views

handler404 = 'views.handler404'

urlpatterns = [
    path('', views.index),
    path('info/', views.get_info),
]
