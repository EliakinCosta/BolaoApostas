from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jogador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(blank=False, null=False, max_digits=18, default=10.0, decimal_places=2)


class Time(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=3)
    #emblema = models.ImageField(blank=True, upload_to='/imagens/emblemas')

    def __str__(self):
        return self.nome


class StatusPartida(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    descricao = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao


class Partida(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    time_casa = models.ForeignKey(Time, related_name='time_casa')
    time_visitante = models.ForeignKey(Time, related_name='time_visitante')
    gols_casa = models.IntegerField(default=0)
    gols_visitante = models.IntegerField(default=0)
    status = models.ForeignKey(StatusPartida)

    def __str__(self):
        return str(self.time_casa) +" X "+ str(self.time_visitante)


class Aposta(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_partida = models.ForeignKey(Partida)
    gols_time_casa = models.IntegerField(default=0)
    gols_time_visitante = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)