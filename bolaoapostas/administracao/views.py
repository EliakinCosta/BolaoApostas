from django.shortcuts import render

# Create your views here.
def base_site(request):
    return render(request, 'administracao/base.html', {})