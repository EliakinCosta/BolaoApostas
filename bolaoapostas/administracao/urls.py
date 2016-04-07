from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.base_site),
    url(r'^$', 'administracao.views.base_site', name='inicio'),
]