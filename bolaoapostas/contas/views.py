from django.shortcuts import render
from administracao.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def painel(request):
    template_name = 'contas/partidas.html'
    partidas = Partida.objects.all()
    return render(request, template_name, {'jogador': queryset_Jogador(request.user),
                                           'partidas': partidas,
                                           'partidas_jogador':get_partidas_apostadas(request.user)})


def queryset_Jogador(usuario):
    return Jogador.objects.get(usuario=usuario)

def get_partidas_apostadas(usuario):
    apostas = Aposta.objects.filter(apostador=queryset_Jogador(usuario))
    partidas = []
    for aposta in apostas:
        partidas.append(aposta.id_partida)
    return partidas

def apostar(request):
    if request.method == 'POST':
        id_partida = request.POST['id_partida']
        jogador = queryset_Jogador(request.user)
        partida = Partida.objects.all().get(id=id_partida)
        print(queryset_apostas_partida_jogador(jogador, partida))
        if queryset_apostas_partida_jogador(jogador, partida):
            return HttpResponse(status_code=400)
        else:
            Aposta.objects.create(
                id_partida=partida,
                gols_time_casa=0,
                gols_time_visitante=0,
                valor=5.00,
                apostador=jogador
            )

            Movimentacao.objects.create(
                 jogador=jogador,
                 valor=-5.00,
            )

            response_data = {}
            response_data['result'] = 'Create post successful!'
            response_data['jogador'] = float(jogador.saldo)

            return JsonResponse(response_data)

def queryset_apostas_partida_jogador(apostador, partida):
    return Aposta.objects.all().filter(apostador=apostador, id_partida=partida)


def sacar_aposta(jogador):
    jogador.saldo = float(jogador.saldo) - 5
    jogador.save(update_fields=["saldo"])

def query_set_apostas_jogador(jogador):
    return Aposta.objects.all().filter(apostador=jogador)


def get_apostas(request):
    template_name = 'contas/apostas.html'
    jogador = queryset_Jogador(request.user)
    return render(request, template_name, {'apostas':query_set_apostas_jogador(jogador)})
    
def ranking(request):
    template_name = 'contas/ranking.html'
    return render(request, template_name, {})