from django import forms
from .models import modelo_Asistente, modelo_Ponente, modelo_Staff

class form_Asistente(forms.ModelForm):
	class Meta:
	      model = modelo_Asistente
	      fields = "__all__" #['campo1','campo2']

class form_Ponente(forms.ModelForm):
	class Meta:
	      model = modelo_Ponente
	      fields = "__all__" #['campo1','campo2']

class form_Staff(forms.ModelForm):
	class Meta:
	      model = modelo_Staff
	      fields = "__all__" #['campo1','campo2']
