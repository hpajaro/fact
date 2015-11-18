from django.http import HttpResponse
from aplic.models import Cliente
from aplic.forms import  ClienteForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.contrib.auth import authenticate, login
def index(request):
	if request.user.is_authenticated():
	    return render_to_response("aplic/index.html",{},
	    context_instance=RequestContext(request))  
	else: 
	   return redirect("/login")


def  clientes(request):
	clientes=Cliente.objects.all()
	"""x="<h1>Lista de Clientes </h1><br>"
	x+="<br>".join(["id:%s,razonSocial: %s,nombreCompleto:%s %s," %(c.id,c.razonSocial,c.nombres,c.apellidos) for c in clientes ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarClientes.html",{'clientes':clientes},
		context_instance=RequestContext(request))

def prueba(request):
	return render_to_response("login",{})

def Crear_cliente(request):
	if request.method =="POST":
		form=ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/clientes")
	else:
		form=ClienteForm()
		return  render_to_response("aplic/CrearClientes.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def Crear_parametro(request):
	if request.method =="POST":
		form=ParametroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/parametro")
	else:
		form=ParametroForm()
		return  render_to_response("aplic/CrearParametro.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))
		