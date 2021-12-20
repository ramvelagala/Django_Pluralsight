from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('listofrooms', views.show_room_objects, name="listofrooms"),
    path('new', views.new, name="new")
]