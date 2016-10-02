from django.db import models

# Create your models here.
class modelo_Asistente(models.Model):
    asistente_name = models.CharField(max_length=24)
    asistente_apellido = models.CharField(max_length=24)
    asistente_edad = models.FloatField()
    asistente_matricula = models.CharField(max_length=24)

    def __str__(self):
        return self.asistente_name


class modelo_Ponente(models.Model):
    ponente_name = models.CharField(max_length=24)
    ponente_apellido = models.CharField(max_length=24)
    ponente_edad = models.FloatField()
    ponente_matricula = models.CharField(max_length=24)

    def __unicode__(self):
        return '%s-%f'%self.asistente_name, self.asistente_type


class modelo_Staff(models.Model):
    staff_name = models.CharField(max_length=24)
    staff_apellido = models.CharField(max_length=24)
    staff_edad = models.FloatField()
    staff_matricula = models.CharField(max_length=24)

    def __unicode__(self):
        return '%s-%f'%self.asistente_name, self.asistente_type
