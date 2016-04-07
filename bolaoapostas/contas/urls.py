from django.conf.urls import url, include

urlpatterns = [
    # O dicionario serve para os parametros que serao passados por parametro para a view de login
    url(r'^entrar/$', 'django.contrib.auth.views.login', {'template_name':'contas/login.html'}, name='login'),
]