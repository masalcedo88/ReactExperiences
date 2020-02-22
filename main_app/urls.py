from django.urls import path
from . import views
# from django.conf.urls import url, include
# from django.contrib import admin
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
  path('', views.index, name='index'),
  path('profile', views.profile, name='profile'),
  path('new_adventure', views.adventure_create, name='adventure_create'),
  path('my_adventures', views.adventures_list, name='adventures_list'),
  path('adventures_offered', views.adventures_offered, name='adventures_offered'),
  path('adventures/<int:pk>', views.adventure_detail, name='adventure_detail'),
  path('book_adventure/<int:pk>', views.book_adventure, name='book_adventure'),
  path('cancel_booking/<int:pk>', views.cancel_booking, name='cancel_booking'),
  # url(r'^search/', include('search.urls', namespace='search')),
]

# if settings.DEBUG:
#     urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
#     urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
