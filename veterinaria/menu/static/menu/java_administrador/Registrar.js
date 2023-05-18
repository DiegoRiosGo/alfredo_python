var nombreReg = document.getElementById('nombreReg');
var correoReg = document.getElementById("correoReg");
var contraReg = document.getElementById("contraReg");
var rutReg = document.getElementById("rutReg");
const formReg = document.getElementById("formReg");
const parrafoReg = document.getElementById("warningsReg")
var errorReg = document.getElementById('errorReg');
errorReg.style.color = 'red';



function enviarformularioReg() {
  console.log('Registrando...');

  var mensajeErrorReg = [];

  if (nombreReg.value === null || nombreReg.value === '') {
    mensajeErrorReg.push('Ingresa tu nombre');
  }
  if (rutReg.value === null || rutReg.value === '') {
    mensajeErrorReg.push('Ingresa tu rut');
  }

  if (correoReg.value === null || correoReg.value === '') {
    mensajeErrorReg.push('Ingresa tu correo');
  }

  if (contraReg.value === null || contraReg.value === '') {
    mensajeErrorReg.push('Ingresa tu contraseña');
  }

  errorReg.innerHTML = mensajeErrorReg.join(', ')

  return false;
}




