from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.


class JogadorAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = User.objects.create_user(username=obj.login, first_name=obj.nome, password=obj.senha, is_active=True)
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(JogadorAdmin, self).get_form(request, obj, **kwargs)
        self.exclude = ('usuario',)
        if obj:
            self.exclude = ('usuario',)
        return form

    def delete_model(self, request, obj):
        obj.user.delete()
        obj.delete()

class PartidaAdmin(admin.ModelAdmin):
    """ """
    def save_model(self, request, obj, form, change):
        if obj:
            if obj.status.id == 2:
                ganhadores, quantidade_apostas = self.get_ganhadores(obj)
                
                for ganhador in ganhadores:
                    ganhador.saldo = float(ganhador.saldo) + float((quantidade_apostas * 5) / len(ganhadores))
                    ganhador.save()
        obj.save()
    
    def get_ganhadores(self, partida):
        apostas = Aposta.objects.all().filter(id_partida = partida)
        
        #Verificar apostas_premiadas por placar
        apostas_premiadas = []
        
        ganhadores = []
        
        for aposta in apostas:
            if (aposta.gols_time_casa == partida.gols_casa and 
                aposta.gols_time_visitante == partida.gols_visitante):
                apostas_premiadas.append(aposta)
        else:
            if not apostas_premiadas:
                for aposta in apostas:
                    if self.get_resultado_aposta(aposta) == self.get_resultado_partida(partida):
                        apostas_premiadas.append(aposta)
                else:
                    if not apostas_premiadas:
                        apostas_premiadas = list(apostas)
        
        if apostas_premiadas:
            for aposta_premiada in apostas_premiadas:
                ganhadores.append(aposta_premiada.apostador)
        
        return ganhadores, len(apostas)
        
        
    #
    def get_resultado_aposta(self, aposta):
        resultado = aposta.gols_time_casa - aposta.gols_time_visitante
        
        if resultado > 0:
            return 1
        elif resultado < 0:
            return -1
        else:
            return 0
            
    def get_resultado_partida(self, aposta):
        resultado = partida.gols_casa - partida.gols_visitante
        
        if resultado > 0:
            return 1
        elif resultado < 0:
            return -1
        else:
            return 0

admin.site.register(Time)
admin.site.register(Partida, PartidaAdmin)
admin.site.register(Aposta)
admin.site.register(StatusPartida)
admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Movimentacao)