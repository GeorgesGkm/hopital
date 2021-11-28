from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^', views.loginPage, name='login_admin'),
    #url(r'^register/$', views.registerPage, name='register'),
    #url(r'^', views.logoutPage, name='Logout'),


]