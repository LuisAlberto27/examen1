from django.shortcuts import render, render_to_response
from .models import modelo_Asistente, modelo_Ponente, modelo_Staff
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .forms import form_Asistente, form_Ponente, form_Staff


class ListaTipoAlmacen(ListView):
    model = modelo_Asistente


# vista de las paginas.
class vista_Inicio(TemplateView):
	template_name = "index.html"

#vista de los datos de la base de datos.
def asistente(request):
	asistente = modelo_Asistente.objects.all()
	return render_to_response('asistentes/asistente.html', {'asistente':asistente})

def ponente(request):
	ponente = modelo_Ponente.objects.all()
	return render_to_response('ponentes/ponente.html', {'ponente':ponente})

def staff(request):
	staff = modelo_Staff.objects.all()
	return render_to_response('staff/staff.html', {'staff':staff})

# vistas de los horarios y de las ponencias
def horario(request):
	horario = modelo_Ponente.objects.all()
	return render_to_response('ponencias/horario.html', {'ponente':ponente})

def conferencia(request):
	conferencia = modelo_Staff.objects.all()
	return render_to_response('ponencias/conferencias.html', {'staff':staff})


#class vista_Asistente(TemplateView):
#	template_name = "asistentes/asistente.html"

# Formularios para las los registros.
class form_Asistente(CreateView):
	template_name = 'asistentes/registro.html'
	model = modelo_Asistente
	fields = '__all__'#[]
	success_url = reverse_lazy('index_view')

class form_Ponente(CreateView):
	template_name = 'ponentes/registro.html'
	model = modelo_Ponente
	fields = '__all__'#[]
	success_url = reverse_lazy('index_view')

class form_Staff(CreateView):
	template_name = 'staff/registro.html'
	model = modelo_Staff
	fields = '__all__'#[]
	success_url = reverse_lazy('index_view')
