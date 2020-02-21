from django.urls import path
from . import views

# Account Routes for Adventure Buddy
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('edit_info/', views.edit_info, name='edit_info'),
]
