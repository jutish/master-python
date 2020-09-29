from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

# Diferencia entre MVC y MVT
# MVC: Modelo vista controlador
# MVT: Modelo vista template - En Django la Vista hace de Controlador. Es este fichero!! y el Template es lo que en otros frameworks es la vista 


layout = """
<h1>Sitio Web - Esteban Marcelloni</h1>
<hr/>
<ul>
	<li><a href="/inicio">Inicio</a></li>
	<li><a href="/hola_mundo">Hola Mundo</a></li>
	<li><a href="/pagina">Pagina de Prueba</a></li>
	<li><a href="/contacto">Contacto</a></li>
</ul>
<hr/>		
"""

def index(request):
	
	html = "<h1>Inicio</h1>"
	html +="<h2>Años pares desde el 2020 al 2050</h2>"
	html +="<ul>"
	cont = 2020
	while cont <= 2050:
		if cont % 2 ==0:
			html += f"<li>Año: {cont}</li>"
		cont+=1
	html +="</ul>"	
	# return HttpResponse(layout+html)
	return render(request,'index.html')

#El request se debe pasar a cada uno de los metodos
def hola_mundo(request):
	# return HttpResponse(layout+"""
	# 	<h1>Hola Mundo con Django!!</h1>
	# 	<h3>Soy Esteban Marcelloni</h3>
	# """)
	return render(request,'hola_mundo.html')

def pagina(request,rdg=0):
	# if rdg==1:
	# 	# return redirect('/contacto/Gavilan/Stefoni') #Aca uso la ruta
	# 	return redirect('contacto',nombre='Gavi', apellido='Marcelloni') #Aca uso el name= definido en la ruta.

	# return HttpResponse(layout+"""
	# 	<h1>Pagina de mi Web</h1>
	# """)
	return render(request,'pagina.html')

def contacto(request,nombre="",apellido=""):
	# return HttpResponse(layout+f"<h2>Contacto {nombre} {apellido}</h2>")
	return render(request,'contacto.html')