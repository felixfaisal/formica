from django.urls import path

from . import views

urlpatterns = [
    path('oauth2/', views.index, name='index'),
    path('oauth2/logout/', views.discord_logout, name='logout'),
    path('oauth2/login/', views.discord_login, name='login'),
    path('oauth2/login/redirect/', views.discord_login_redirect, name='loginredirect'),
    path('api/forms/', views.formlist, name='formlist'), 
    path('api/responses/', views.responselist, name='responselist'), 
    path('api/formcreate/', views.formcreateresponse, name='formcreateresponse'), 
    path('api/formresponse/<str:FormName>', views.formresponse, name='formresponse')
]