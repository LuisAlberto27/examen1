from django.db import models

# Create your models here.
class modelo_Asistente(models.Model):
    Nombre_Asistente = models.CharField(max_length=24, help_text='Nombre del Asistente.', unique='true')
    Apellido_Asistente = models.CharField(max_length=24, help_text='Apellido del Asistente.')
    Asistir_Ponencia = models.CharField(max_length=24, help_text='Ponencia A la Que desea Asistir.')
    Correo_Asistente = models.CharField(max_length=24, help_text='Correo del Asistente.')
    Telefono_Asistente = models.CharField(max_length=15,help_text='Telefono del Asistente.')

    def __str__(self):
        return self.Nombre_Asistente

HORA_CHOICES = (
    ('N/D', 'Seleccione Horario'),
    ('12:00 PM - 1:00 PM.', '12:00 PM - 1:00 PM'),
    ('1:00 PM - 2:00 PM.', '1:00 PM - 2:00 PM'),
    ('2:00 PM - 3:00 PM.', '2:00 PM - 3:00 PM'),
    ('3:00 PM - 4:00 PM.', '3:00 PM - 4:00 PM'),
    ('4:00 PM - 5:00 PM.', '4:00 PM - 5:00 PM'),
    ('5:00 PM - 6:00 PM.', '5:00 PM - 6:00 PM'),
    ('6:00 PM - 7:00 PM.', '6:00 PM - 7:00 PM'),
    ('7:00 PM - 8:00 PM.', '7:00 PM - 8:00 PM'),
    ('8:00 PM - 9:00 PM.', '8:00 PM - 9:00 PM'),
    ('9:00 PM - 10:00 PM.', '9:00 PM - 10:00 PM'),
)

class modelo_Ponente(models.Model):
    Titulo_Ponencia = models.CharField(max_length=24, help_text='Titulo De La ponencia.', unique='true')
    Nombre_Ponente = models.CharField(max_length=15, help_text='Nombre Del Ponente.')
    Apellido_Ponente = models.CharField(max_length=24, help_text='Apellido Del Ponente.')
    Hora_Ponencia = models.CharField(choices=HORA_CHOICES,max_length=15,default='0', help_text='Hora De La Ponencia.', unique='true')
    Correo_Ponente = models.CharField(max_length=24, help_text='Correo del Ponente.')
    Telefono_Ponente = models.CharField(max_length=15, help_text='Telefono del Ponente.')

    def __str__(self):
        return '%s -- %s' % (self.Titulo_Ponencia, self.Nombre_Ponente)

class modelo_Staff(models.Model):
    Nombre_Staff = models.CharField(max_length=24, help_text='Nombre De Staff.')
    Apellido_Staff = models.CharField(max_length=24, help_text='Apellido De Staff.')
    Puesto_Staff = models.CharField(max_length=24, help_text='Puesto De Staff.')
    Correo_Staff = models.CharField(max_length=24, help_text='Correo De Staff.')
    Telefono_Staff = models.CharField(max_length=15, help_text='Telefono De Staff.')

    def __str__(self):
        return self.Nombre_Staff
