from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('adventures/new', views.adventure_create, name='adventure_create'),
]