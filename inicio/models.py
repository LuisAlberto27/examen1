from django.db import models

# Create your models here.
class modelo_Asistente(models.Model):
    Nombre_Asistente = models.CharField(max_length=24)
    Apellido_Asistente = models.CharField(max_length=24)
    Asistir_Ponencia = models.CharField(max_length=24)
    Correo_Asistente = models.CharField(max_length=24)
    Telefono_Asistente = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre_Asistente


class modelo_Ponente(models.Model):
    Titulo_Ponencia = models.CharField(max_length=24)
    Nombre_Ponente = models.CharField(max_length=15)
    Apellido_Ponente = models.CharField(max_length=24)
    Dia_Ponencia = models.CharField(max_length=24)
    Hora_Ponencia = models.FloatField()
    Correo_Ponente = models.CharField(max_length=24)
    Telefono_Ponente = models.CharField(max_length=15)

    def __str__(self):
        return '%s-%f'%self.Titulo_Ponencia, self.Nombre_Ponente


class modelo_Staff(models.Model):
    Nombre_Staff = models.CharField(max_length=24)
    Apellido_Staff = models.CharField(max_length=24)
    Puesto_Staff = models.CharField(max_length=24)
    Correo_Staff = models.CharField(max_length=24)
    Telefono_Staff = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre_Staff
