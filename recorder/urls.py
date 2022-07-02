from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_child/', views.add_child, name='add_child')
]