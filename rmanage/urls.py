from django.conf.urls import url

from . import views

app_name = 'rmanage'
company_url = "r'^company/(?P<company>[A-Za-z0-9]+)"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/$', views.advert, name='advert'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/apply/$', views.apply_into, name='apply_into'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/manage/$', views.manage, name='manage'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/notices/$', views.see_notices, name='see_notices'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/rdrive/$', views.rdrive, name='rdrive'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/create/$', views.create_rdrive, name='create_rdrive'),
]
