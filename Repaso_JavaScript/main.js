alert("Repasando JavaScript")
var nombre = "Fernando Baculima"
var altura = 170;
var concatenacion = nombre + " " + altura
//document.write(concatenacion)
var datos = document.getElementById("datos")
datos.innerHTML = concatenacion

/*
datos2.innerHTML = "<h1> Hola desde datos 2 </h1> <h3> Mi nombre es: </h3>" + nombre;

if(altura <= 190){
    datos2.innerHTML += '<h1>No eres una persona alta</h1>'
}

for (var i = 0;i<20;i++){
    //bloque de instrucciones
    datos2.innerHTML += '<h2>Este es el contador: </h2>' + i
}


*/
function MuestraMiNombre(nombre, altura){
    var datos2 = document.getElementById("datos2")
    datos2.innerHTML = "<h1> Hola desde datos 2 </h1> " +
                        "<h3> Mi nombre es: </h3>" + nombre;

    if(altura <= 190){
        datos2.innerHTML += '<h1>No eres una persona alta</h1>'
    }

    for (var i = 0;i<20;i++){
        //bloque de instrucciones
        datos2.innerHTML += '<h2>Este es el contador: </h2>' + i
    }
}


MuestraMiNombre(nombre, altura)

var nombres=['Fernando', 'John']
alert(nombres[1])
document.write('Listado de Nombres <br>' )
for (i = 0; i< nombres.length; i++){
    document.write(nombres[i]+'<br>')
}

document.write('Listado de Nombres con funcion de callback <br>' )
nombres.forEach(function (nombre){
    document.write(nombre+'<br>')
})
document.write('Listado de Nombres con funcion de callback, de flecha <br>' )
nombres.forEach((nombre) =>{
    document.write(nombre+'<br>')
})