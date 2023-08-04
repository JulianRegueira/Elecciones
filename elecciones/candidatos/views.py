from django.shortcuts import render
from .models import candidato
from django.http import Http404

def index(request):
    candidatos = candidato.objects.all()
    return render(request, 'index.html', {'candidatos': candidatos})

def votar(request, candidato_id):
    try:
        candidato_votado = candidato.objects.get(pk=candidato_id)
    except candidato.DoesNotExist:
        raise Http404("El candidato no existe.")

    candidato_votado.cantidad_de_votos += 1
    candidato_votado.save()

    return render(request, 'gracias.html')