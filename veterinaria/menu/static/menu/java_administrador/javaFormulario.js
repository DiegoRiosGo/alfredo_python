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


var respuesta =document.getElementById(r);
var respuesta1 =document.getElementById(r1);
var respuesta2 =document.getElementById(r2);
var respuesta3=document.getElementById(r3);
var respuesta4 =document.getElementById(r4);




function enviarformulario_contacto_con_cliente(){
    console.log('Enviando');

    var MensajeError =[];

    if(r.value=== null||r.value=== ''){
        MensajeError.push('Debe colocar una respuesta')
    }


    error.innerHTML =MensajeError.join(', ')
    return false;

}

function enviarformulario_contacto_con_cliente1(){
    console.log('Enviando');

    var MensajeError =[];

    if(r1.value=== null||r1.value=== ''){
        MensajeError.push('Debe colocar una respuesta a este campo')

    error.innerHTML =MensajeError.join(', ')
    return false;

}


}

function enviarformulario_contacto_con_cliente2(){
    console.log('Enviando');

    var MensajeError =[];

    if(r2.value=== null||r2.value=== ''){
        MensajeError.push('Debe colocar una respuesta a este campo')

    error.innerHTML =MensajeError.join(', ')
    return false;

}
}

function enviarformulario_contacto_con_cliente3(){
    console.log('Enviando');

    var MensajeError =[];

    if(r3.value=== null||r3.value=== ''){
        MensajeError.push('Debe colocar una respuesta a este campo')

    error.innerHTML =MensajeError.join(', ')
    return false;

}
}

function enviarformulario_contacto_con_cliente3(){
    console.log('Enviando');

    var MensajeError =[];

    if(r4.value=== null||r4.value=== ''){
        MensajeError.push('Debe colocar una respuesta a este campo')

    error.innerHTML =MensajeError.join(', ')
    return false;

}
}