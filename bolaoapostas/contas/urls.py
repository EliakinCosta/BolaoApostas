from django.conf.urls import url, include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    # O dicionario serve para os parametros que serao passados por parametro para a view de login
    url(r'^$', views.painel, name='painel'),
    url(r'^entrar/$', auth_view.login , {'template_name':'contas/login.html'}, name='login'),
    url(r'^sair/$', auth_view.logout, {'next_page':'administracao:inicio'}, name='logout'),
    url(r'^apostar/', views.apostar),
]