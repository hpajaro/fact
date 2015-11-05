from django.http import HttpResponse
from aplic.models import Cliente
from django.shortcuts import get_object_or_404, render_to_response
def  index(request):
	clientes=Cliente.objects.all()
	"""x="<h1>Lista de Clientes </h1><br>"
	x+="<br>".join(["id:%s,razonSocial: %s,nombreCompleto:%s %s," %(c.id,c.razonSocial,c.nombres,c.apellidos) for c in clientes ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listar.html",{'clientes':clientes})

def prueba(request):
	return render_to_response("aplic/index.html",{})