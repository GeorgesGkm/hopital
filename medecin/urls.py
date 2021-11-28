from django.conf.urls import url

from medecin import views

urlpatterns = [
    url(r'^medecin/patient', views.medecin_grille_list, name='medecin_grille_list'),
    url(r'^medecin/liste', views.medecin_list, name='medecin_list'),
    url(r'^medecins/create$', views.medecins_create, name='medecins_create'),
    #url(r'^medecins/(?P<pk>\d+)/delete/$', views.medecins_delete, name='medecins_delete'),
    #url(r'^medecins/(?P<pk>\d+)/update/$', views.medecins_update, name='medecins_update'),
]