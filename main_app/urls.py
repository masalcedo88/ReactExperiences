from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('new_adventure', views.adventure_create, name='adventure_create'),
  path('my_adventures', views.adventures_list, name='adventures_list'),
]