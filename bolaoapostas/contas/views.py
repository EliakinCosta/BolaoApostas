from django.shortcuts import render
from administracao.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def painel(request):
    template_name = 'contas/partidas.html'
    partidas = Partida.objects.all()
    return render(request, template_name, {'jogador':queryset_Jogador(request.user), 'partidas':partidas})

def queryset_Jogador(usuario):
    lista_contem_jogador = Jogador.objects.all().filter(usuario=usuario).values()
    jogador = list(lista_contem_jogador)[0]
    return jogador