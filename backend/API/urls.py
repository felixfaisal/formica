from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.tasklist, name='list'),
    path('logout/', views.discord_logout, name='logout'),
    path('listcreate/', views.listcreate, name='listcreate'), 
    path('listdetail/<str:pk>/', views.taskdetail, name='listdetail'),
    path('listupdate/<str:pk>/', views.listupdate, name='listupdate'),
    path('listdelete/<str:pk>/', views.listdelete, name='listdelete'),
    path('login/', views.discord_login, name='login'),
    path('login/redirect/', views.discord_login_redirect, name='loginredirect'),
    path('forms/', views.formlist, name='formlist'), 
    path('responses/', views.responselist, name='responselist')
]