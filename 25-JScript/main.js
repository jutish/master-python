
var nombre = "Esteban Marcelloni ";
var altura = "1.7"

var concatenacion = nombre+" "+altura;
// alert("Hola "+nombre);
document.write(concatenacion); //Agrega la variable al documento
document.write(altura);

var datos = document.getElementById("datos");
datos.innerHTML = concatenacion; //Agrega la variable al elemento con id "datos"

var datos2 = document.getElementById("datos2");
datos2.innerHTML = `
	<h2>Hola soy un innerHTML</h2>
	<h3>Bienvenido ${nombre}</h3>
	<h4>Mido ${altura}</h4>
`;


altura2 = 1.60
if(altura2 > 1.65){
	datos2.innerHTML += `<h1>Eres alto ${nombre}</h1>` //Con += concatenamos el cont. de datos2 con lo nuevo
}else{
	datos2.innerHTML += `<h1>Eres promedio ${nombre}</h1>`
}

for(var i=2010;i<=2020;i++){
	datos2.innerHTML += `<p>Estamos en el año ${i}</p>`	
}

function muestraNombre(nombre,altura){
	res = "Hola "+nombre+ " tu mides: "+altura
	return res
}

function imprimir(){
	alert(muestraNombre("Esteban",1.70))
} 

imprimir()

var nombres = ['Victor', 'Antonio','Esteban']

for(i=0;i<nombres.length;i++){
	document.write	("<br>Nombre: "+nombres[i])
}

//Usando funcion anonima
nombres.forEach(function(nombre){
	document.write("<br> Nombre:"+nombre)
})
//Usando funcion de flecha
nombres.forEach((nombre)=>{
	document.write("<br> Tu Nombre:"+nombre)	
})


