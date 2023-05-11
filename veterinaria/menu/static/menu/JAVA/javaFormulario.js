
/*Crear cuenta*/

var nombre = document.getElementById('nombre');
var correo = document.getElementById("correo");
var contraseña = document.getElementById("contraseña");
var contraseña_nueva = document.getElementById("contraseña_nueva");

/*Contacto*/

var nombre_contacto = document.getElementById('nombre_contacto');
var correo_contacto = document.getElementById("correo_contacto");
var nro_contacto = document.getElementById("nro_contacto");
var nombre_m_contacto = document.getElementById("nombre_m_contacto");
var msg_contacto = document.getElementById("msg_contacto");

/*Agenda online*/

const form = document.getElementById("form");
const parrafo = document.getElementById("warnings");
var error = document.getElementById('error');
error.style.color = "red";
error.style.textAlign = "center";


/*Formulario Crear cuenta */

function enviarformulario() {
    console.log('Registrando...');

    var mensajeError = []

    if (nombre.value === null || nombre.value === '') {
        mensajeError.push('Ingresa tu nombre');
    }
    else
        if (nombre.value.length < 10 || nombre.value.length > 15) {
            mensajeError.push('El nombre debe tener entre 10 y 15 caracteres');
        }


    if (correo.value === null || correo.value === '') {
        mensajeError.push('Ingresa tu correo');
    }
    

    if (contraseña.value === null || contraseña.value === '') {
        mensajeError.push('Ingresa tu contraseña');
    }
    else
        if (contraseña.value.length < 6 || contraseña.value.length > 12) {
            mensajeError.push('La contraseña debe tener entre 6 y 12 caracteres');
        }



    else
        if (contraseña_nueva.value.length < 6 || contraseña_nueva.value.length > 12) {
            mensajeError.push('La contraseña debe tener entre 6 y 12 caracteres');
        }

        if(contraseña.value != contraseña_nueva.value){
            mensajeError.push('Las contraseñas deben coincidir')
           contraseña.value ="";
           contraseña_nueva.value = ""; 
            contraseña.focus();
        }
    else
    mensajeError.push('');


    error.innerHTML = mensajeError.join(', ')

    return false;
}

/*CONTACTO*/

function enviarformulario_contacto() {
    console.log('Registrando...');

    var mensajeError = [];

    if (nombre_contacto.value === null || nombre_contacto.value === '') {
        mensajeError.push('Ingresa tu nombre');
    }
    else
        if (nombre_contacto.value.length < 4 || nombre_contacto.value.length > 30){
        mensajeError.push('El nombre debe tener entre 4 a 30 caracateres')
    }
    if (correo_contacto.value === null || correo_contacto.value === '') {
        mensajeError.push('Ingresa tu correo');
    }

    if  (nro_contacto.value === null || nro_contacto.value === '') {
        mensajeError.push('Ingresa tu número');
    }
    else
        if(nro_contacto.value.length<9 ||nro_contacto.value.length>13){
            mensajeError.push('El teléfono debe de tener 11 caracteres')
        }

    if (nombre_m_contacto.value === null || nombre_m_contacto.value === '') {
        mensajeError.push('Ingresa el nombre de tu mascota');
    }
    else
    if (nombre_m_contacto.value.length <4 || nombre_m_contacto.value.length > 15)
    mensajeError.push('El nombre debe tener entre 4 a 15 caracteres.')

    if (msg_contacto.value === null || msg_contacto.value === '') {
        mensajeError.push('Ingresa el mensaje');
    }
    else
        if (msg_contacto.value.length > 50) {
            mensajeError.push('La cantidad maxima de caracteres es de 50');
        }

    error.innerHTML = mensajeError.join(', ')

    return false;



}
/*Formulario Agenda*/

var username = document.getElementById('username');
var email = document.getElementById("email");
var tipo = document.getElementById("tipo");
var file = document.getElementById("file");
var arrive = document.getElementById("arrive");
var textarea2 = document.getElementById("textarea2");

function enviarformulario_agenda() {
    console.log('Registrando...');

    var mensajeError = [];

    if (username.value === null || username.value === '') {
        mensajeError.push('Ingresa tu nombre');
    }
    if (email.value === null || email.value === '') {
        mensajeError.push('Ingresa tu correo');
    }

    if (tipo.value === null || tipo.value === '') {
        mensajeError.push('Ingresa tu número');
    }
    if (tipo.value === null || tipo.value === '') {
        mensajeError.push('Ingresa tu número');
    }

    if (file.value === null || file.value === '') {
        mensajeError.push('Ingresa una imagen');
    }

    if (arrive.value === null || arrive.value === '') {
        mensajeError.push('Ingresa fecha de reserva');
    }








    error.innerHTML = mensajeError.join(', ')

    return false;
}

/*Inicio Sesion*/
var correolog = document.getElementById("correolog");
var contralog = document.getElementById("contralog");
var errorlog = document.getElementById("errorlog");
errorlog.style.color = "red";



function enviaformlog() {
    console.log('Registrando...');

    var mensajeErrorLog = [];

    if (correolog.value === null || correolog.value === '') {
        mensajeErrorLog.push('Ingresa tu correo');
    }

    if (contralog.value === null || contralog.value === '') {
        mensajeErrorLog.push('Ingresa tu contraseña');
    }
    else
        if (contralog.value.length < 6 || contralog.value.length > 12) {
            mensajeErrorLog.push('La contraseña debe tener entre 6 y 12 caracteres');
        }



    errorlog.innerHTML = mensajeErrorLog.join(', ')

    return false;
}

function validarCorreo(correo) {
    const expresion = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    return expresion.test(correo);
}

