from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('add-room/', views.add_room, name='add_room'),
    path('add-guest/', views.add_guest, name='add_guest'),
]
