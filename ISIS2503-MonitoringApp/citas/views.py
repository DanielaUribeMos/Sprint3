from django.http import JsonResponse
from django.shortcuts import render
from plantillas.logic.logic_plantilla import get_plantillas
from .logic.logic_cita import get_citas, create_cita

def cita_list(request):
    citas = get_citas()
    context = list(citas.values())
    return JsonResponse(context, safe=False)

def generate_cita(request):
    plantillas = get_plantillas()
    for plantilla in plantillas:
        if plantilla.especificacion == 'Emergencia':
            cita = create_cita()
            return JsonResponse(cita.toJson(), safe=False)
        else:
            return JsonResponse({'message': 'No cita created'}, status=200)