# Entrega1_Echenique
Web Django - Entrega intermedia trabajo final Coder


# Hola
Esto es una pagina cuyo objetivo es recoger datos para guardar en BBDD.

# Primero
luego de iniciar mi proyecto en git y una vez creado el mvt, desde views.py importo los elementos de un response:
-from django.http import HttpResponse
creo la funcion "inicio" y lo importo desde urls.py
-from mi_app.views import inicio
-path('WebProject/', inicio)
creo la carpeta templates y otra carpeta dentro que contiene el html con la vista de mi inicio.