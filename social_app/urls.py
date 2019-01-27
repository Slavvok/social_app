from django.urls import path
from . import views

<<<<<<< HEAD
handler404 = views.handler404
=======
handler404 = 'views.handler404'
>>>>>>> 01d4c024dddf9375ac7ccc3c3b76d69333713388

urlpatterns = [
    path('', views.index),
    path('info/', views.get_info),
]
