from django.urls import path

from . import views

urlpatterns = [
    path('oauth2/logout/', views.discord_logout, name='logout'),
    path('oauth2/login/', views.discord_login, name='login'),
    path('oauth2/login/redirect/', views.discord_login_redirect, name='loginredirect'),
    path('api/form/list', views.formlist, name='formlist'),
    path('api/form/create/', views.formcreateresponse, name='formcreateresponse'),
    path('api/form/response/<str:FormName>', views.formresponse, name='formresponse'),
    path('api/user/create/', views.userCreate, name='userCreate'),
    path('api/user/login/', views.userLogin, name='userLogin'),
    path('api/user/logout/', views.userLogout, name='userLogout'),
    path('api/user/server/', views.userServers, name='userServer'),
    path('api/user/channels/<str:ServerID>', views.serverChannels, name='serverChannels'),
    path('api/user/information', views.userInformation, name='userInformation'),
    path('api/bot/forms/<str:serverid>', views.botFormList, name='botFormList'),
    path('api/bot/response/', views.botFormResponse, name='botFormResponse'),
    path('api/user/dashboard', views.dashboardInformation, name='dashboardInformation'),
    path('api/bot/form/response/<str:FormName>', views.botFormResponseList, name='botFormResponseList'),
    path('api/user/responses', views.userResponses, name='userResponses')
]
