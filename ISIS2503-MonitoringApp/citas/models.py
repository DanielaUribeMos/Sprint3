from django.db import models
from historias.models import Historia
from plantillas.models import Plantilla

class Cita(models.Model):
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"dateTime": %s}' % (self.dateTime.nombre)
    
    def toJson(self):
        cita = {
            'dateTime': self.dateTime,
        }
        return cita