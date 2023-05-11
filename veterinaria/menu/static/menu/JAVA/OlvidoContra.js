var correoOlvida = document.getElementById("correoOlvida");
var contraOlvida = document.getElementById("contraOlvida");
var contraNueva = document.getElementById("contraNueva");
const formOlvida= document.getElementById("formOlvida")
const parrafoOlvida = document.getElementById("warningsOlvida");
var errorOlvida = document.getElementById('errorOlvida');
errorOlvida.style.color='red';

//OLVIDAR CONTRASEÑA

function enviaformolvida() {
  console.log('Registrando...');

  var mensajeErrorOlvida = [];

  if (correoOlvida.value === null || correoOlvida.value === '') {
    mensajeErrorOlvida.push('Ingresa tu correo');
  }

  if (contraOlvida.value === null || contraOlvida.value === '') {
    mensajeErrorOlvida.push('Ingresa tu contraseña');
  }
  else
    if (contraOlvida.value.length < 6 || contraOlvida.value.length > 12) {
      mensajeErrorOlvida.push('La contraseña debe tener entre 6 y 12 caracteres');
    }

  if (contraNueva.value === null || contraNueva.value === '') {
    mensajeErrorOlvida.push('Ingresa tu contraseña otra vez');
  }
  else
    if (contraNueva.value.length < 6 || contraNueva.value.length > 12) {
      mensajeErrorOlvida.push('La contraseña debe tener entre 6 y 12 caracteres');
    }

  errorOlvida.innerHTML = mensajeErrorOlvida.join(', ')

  return false;
}