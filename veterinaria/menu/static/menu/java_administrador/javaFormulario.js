var nombre_mascota = document.getElementById('nombre_mascota');
var nombre_dueño = document.getElementById("nombre_dueño");
var enfermedades = document.getElementById("enfermedades");
var años_mascota= document.getElementById("años_mascota")
var error = document.getElementById('error');
error.style.color = 'red';
error.style.fontSize='small';



function enviarformulario_r(){
     console.log('Registrando...');

    var mensajeError = [];

    if(nombre_mascota1.value === null||nombre_mascota1.value === ''){
        mensajeError.push('Ingresa el nombre de tu mascota');
    }
    if(nombre_dueño1.value === null||nombre_dueño1.value === ''){
        mensajeError.push('Ingresa tu nombre');
    }

    if(enfermedades1.value === null||enfermedades1.value === ''){
        mensajeError.push('Llena el campo de "enfermedades"');
    }

    if(años_mascota1.value === null||años_mascota1.value === ''){
        mensajeError.push('Ingresa la edad de tu mascota');
    }






      error.innerHTML =  mensajeError.join(', ')

    return false;
}






