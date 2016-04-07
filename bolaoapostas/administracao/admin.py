from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
# Register your models here.

class JogadorInline(admin.StackedInline):
    model = Jogador
    verbose_name_plural = 'Jogador'

# Define a new User admin
class UserAdmin(admin.ModelAdmin):
    inlines = (JogadorInline, )

admin.site.register(Time)
admin.site.register(Partida)
admin.site.register(Aposta)
admin.site.register(StatusPartida)