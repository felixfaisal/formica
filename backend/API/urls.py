from django.urls import path

from . import views

urlpatterns = [
    path('oauth2/', views.index, name='index'),
    path('oauth2/logout/', views.discord_logout, name='logout'),
    path('oauth2/login/', views.discord_login, name='login'),
    path('oauth2/login/redirect/', views.discord_login_redirect, name='loginredirect'),
    path('api/form/list', views.formlist, name='formlist'), 
    path('api/responses/', views.responselist, name='responselist'), 
    path('api/form/create/', views.formcreateresponse, name='formcreateresponse'), 
    path('api/form/response/<str:FormName>', views.formresponse, name='formresponse'),
    path('api/user/create/', views.userCreate, name='userCreate'), 
    path('api/user/login/', views.userLogin, name='userLogin'), 
    path('api/user/logout/', views.userLogout, name='userLogout'), 
    path('api/user/server/', views.userServers, name='userServer'), 
    path('api/user/channels/<str:ServerID>', views.serverChannels, name='serverChannels')
]