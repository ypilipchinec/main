from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screens_status/<str:names>/<str:status>/<str:created_at>', views.screens_status, name='screens_status'),
    path('show_camers/<str:types>', views.show_camers, name='show_camers'),
    #path(r'^form_camers/$', views.form_camers),
    #re_path(r'form_camers/(?P<type>[^/]+)/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', views.form_camers)
    path('form_camers/<str:type>/<int:id>/create', views.form_camers, name='form_camers'),
    path('form_camers/<str:type>/<int:id>/edit', views.form_camers, name='form_camers')
]

