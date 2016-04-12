from django.db import models
from django.contrib.auth.models import User
from ajaximage.fields import AjaxImageField

# Create your models here.


class Jogador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=55, null=False, blank=False)
    login = models.CharField(max_length=55, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=25, null=False, blank=False)
    saldo = models.DecimalField(decimal_places=2, max_digits=18, default=10.00)

class Time(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    sigla = models.CharField(max_length=3, blank=False, null=False)
    emblema = AjaxImageField(blank=True, upload_to='imagens/emblemas')

    def __str__(self):
        return self.nome


class StatusPartida(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    descricao = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.descricao


class Partida(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    time_casa = models.ForeignKey(Time, related_name='time_casa', blank=False, null=False)
    time_visitante = models.ForeignKey(Time, related_name='time_visitante', blank=False, null=False)
    gols_casa = models.IntegerField(default=0, blank=False, null=False)
    gols_visitante = models.IntegerField(default=0, blank=False, null=False)
    status = models.ForeignKey(StatusPartida, blank=False, null=False)

    def __str__(self):
        return str(self.time_casa) + " x " + str(self.time_visitante)


class Aposta(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_partida = models.ForeignKey(Partida, blank=False, null=False)
    apostador = models.ForeignKey(Jogador, blank=False, null=False)
    gols_time_casa = models.IntegerField(default=0, blank=False, null=False)
    gols_time_visitante = models.IntegerField(default=0, blank=False, null=False)
    valor = models.DecimalField(max_digits=3, decimal_places=2, default=5.0, blank=False, null=False)

    def __str__(self):
        return str(self.id_partida) + " " + str(self.gols_time_casa) + " x " + str(self.gols_time_visitante)


class Movimentacao(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    jogador = models.ForeignKey(Jogador)
    valor = models.DecimalField(decimal_places=2, max_digits=18, default=10.00)