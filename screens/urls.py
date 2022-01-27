from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('screens_status/<str:names>/<str:status>/<str:created_at>', views.screens_status, name='screens_status'),
    path('show_camers/<str:types>', views.show_camers, name='show_camers'),
    #re_path(r'form_camers/(?P<type>[^/]+)/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', views.form_camers)
    path('camers/create/', views.create_camers, name='create_camers'),
    path('camers/<int:id>/edit', views.edit_camers, name='edit_camers')
]

