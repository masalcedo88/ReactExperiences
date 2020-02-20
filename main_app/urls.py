from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('new_adventure', views.adventure_create, name='adventure_create'),
  path('my_adventures', views.adventures_list, name='adventures_list'),
  path('adventures_offered', views.adventures_offered, name='adventures_offered'),
  path('adventures/<int:pk>', views.adventure_detail, name='adventure_detail'),
  path('book_adventure/<int:pk>', views.book_adventure, name='book_adventure'),
]