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



admin.site.register(Time)
admin.site.register(Partida)
admin.site.register(Aposta)
admin.site.register(StatusPartida)
admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Movimentacao)