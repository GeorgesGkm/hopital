from django.conf.urls import url

from specialiste import views

urlpatterns = [
    url(r'^specialiste/$', views.specialiste_list, name='specialiste_list'),
    url(r'^specialiste/suivi', views.etape1_list, name='etape1_list'),
    url(r'^specialiste/create$', views.specialiste_create, name='specialiste_create'),
    #url(r'^medecins/(?P<pk>\d+)/delete/$', views.medecins_delete, name='medecins_delete'),
    #url(r'^medecins/(?P<pk>\d+)/update/$', views.medecins_update, name='medecins_update'),
]