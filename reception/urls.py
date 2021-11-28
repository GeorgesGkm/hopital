from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^books/create$', views.book_create, name='book_create'),
    url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
    url(r'^entreprise/$', views.entreprise_list, name='entreprise_list'),
    url(r'^entreprise/create$', views.entreprise_create, name='entreprise_create'),
    url(r'^services/$', views.service_list, name='service_list'),
    url(r'^service/create$', views.service_create, name='service_create'),
    url(r'^service/(?P<pk>\d+)/update/$', views.service_update, name='service_update'),
    url(r'^service/(?P<pk>\d+)/delete/$', views.service_delete, name='service_delete')
]