from django.db import models
from historias.models import Historia
from plantillas.models import Plantilla

class Cita(models.Model):
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"plantilla": %s}' % (self.plantilla.nombre)
    
    def toJson(self):
        cita = {
            'plantilla': self.plantilla.nombre,
            'dateTime': self.dateTime,
        }
        return cita