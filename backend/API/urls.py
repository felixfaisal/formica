from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oauth2/logout/', views.discord_logout, name='logout'),
    path('api/listcreate/', views.listcreate, name='listcreate'), 
    path('oauth2/login/', views.discord_login, name='login'),
    path('oauth2/login/redirect/', views.discord_login_redirect, name='loginredirect'),
    path('api/forms/', views.formlist, name='formlist'), 
    path('api/responses/', views.responselist, name='responselist'), 
    path('api/formcreate/', views.formcreateresponse, name='formcreateresponse')
]