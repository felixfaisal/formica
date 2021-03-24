from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tasklist, name='list'),
    path('listcreate/', views.listcreate, name='listcreate')
]