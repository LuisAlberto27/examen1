from django.contrib import admin
from .models import modelo_Asistente, modelo_Ponente, modelo_Staff

admin.site.register(modelo_Asistente)
admin.site.register(modelo_Ponente)
admin.site.register(modelo_Staff)
