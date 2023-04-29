from django.http import JsonResponse
from django.shortcuts import render
from plantillas.logic.logic_plantilla import get_plantillas
from .logic.logic_cita import get_citas, create_cita
from historias.logic.historia_logic import get_historia_by_name

def cita_list(request):
    citas = get_citas()
    context = list(citas.values())
    return JsonResponse(context, safe=False)

def generate_cita(request, plantilla_nivel):
    plantillas = get_plantillas()
    createcita = False
    for plantilla in plantillas:
        if plantilla.especificacion == 'Emergencia':
            createCita = True
    if createcita:
        cita = create_cita(plantilla)
        return JsonResponse(cita.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No cita created'}, status=200)