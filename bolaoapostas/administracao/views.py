from django.shortcuts import render

# Create your views here.
def abrir_login(request):
    return render(request, 'administracao/login.html', {})