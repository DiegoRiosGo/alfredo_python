var correoLogJuan = document.getElementById("correoLogJuan");
var contraLogJuan = document.getElementById("contraLogJuan");
const formLogJuan = document.getElementById("formLogJuan");
const parrafoLogJuan = document.getElementById("warningsLogJuan");
var errorLogJuan = document.getElementById('errorLogJuan');
errorLogJuan.style.color = 'red';



function enviaLogJuan() {
  console.log('Iniciando Sesion...');

  var mensajeErrorLogJuan = [];

  if (correoLogJuan.value === null || correoLogJuan.value === '') {
    mensajeErrorLogJuan.push('Ingresa tu correo');
  }

  if (contraLogJuan.value === null || contraLogJuan.value === '') {
    mensajeErrorLogJuan.push('Ingresa tu contraseña');
  }






  errorLogJuan.innerHTML = mensajeErrorLogJuan.join(', ')

  return false;
}
























