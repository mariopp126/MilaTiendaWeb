<<<<<<< HEAD
# tienda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('opiniones/', views.opiniones, name='opiniones'),
]
=======
# tienda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('opiniones/', views.opiniones, name='opiniones'),
]
>>>>>>> 7626d6ba41a4555c94be89f1fd3cf53cbaf4826e
