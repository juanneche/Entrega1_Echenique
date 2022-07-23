from django.shortcuts import render

from django.http import HttpResponse
from mi_app.forms import PersonaFormulario

def inicio(request):

      return render(request, "mi_app/inicio.html")


def Formulario(request):
      if request.method == 'POST':
            miFormulario = PersonaFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  persona = Persona(nombre=informacion['nombre'], edad=informcion['edad'])
                  persona.save()
                  return render(request, "mi_app/inicio.html")
      else
           miFormulario= PersonaFormulario()
      return render(request, "mi_app/Formulario.html",{"miFormulario":miFormulario})

def busquedaNombre(request):
      return render (request, "mi_app/busquedaNombre.html")

def buscar(request):
      respuesta = f"Estoy buscando el nombre: {request.GET['nombre']}"
      return HttpResponse(respuesta)