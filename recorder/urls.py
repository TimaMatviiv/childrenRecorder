from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_child/', views.add_child, name='add_child'),
    path('child/<int:child_id>', views.child, name='child'),
    path('delete_child/<int:child_id>', views.delete_child, name='delete_child')
]