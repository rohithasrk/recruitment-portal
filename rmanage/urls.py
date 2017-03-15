from django.conf.urls import url

app_name = 'rmanage'
company_url = "r'^company/(?P<company>[A-Za-z0-9]+)"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.collab_login, name='collab_login'),
    url(r'^logout/$', views.collab_logout, name='collab_logout'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/$', views.advert, name='advert'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/apply/$', views.apply_into, name='apply_into'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/manage/$', views.manage, name='manage'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/notices/$', views.see_notices, name='see_notices'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/rdrive/(?P<r_id>(\d+))$', views.rdrive, name='rdrive'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/rdrive/(?P<r_id>(\d+))/panel$', views.rdrive, name='add_panel'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/rdrive/createnew/$', views.rdrive_create, name='rdrive_create'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/panel/$', views.panel, name='panel'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/panel/createpanel/$', views.create_panel, name='create_panel'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/addMembers/$', views.add_members, name='add_members'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/addNotice/$', views.add_notice, name='add_notice'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/candidate/$', views.view_candidates, name='view_candidates'),
    url(r'^company/(?P<company>[A-Za-z0-9]+)/rdrive/(?P<year>[0-9]+)/(?P<role>[A-Za-z0-9])/$', views.rdrive_edit, name='rdrive_edit'),
]
