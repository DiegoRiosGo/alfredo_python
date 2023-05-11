/*
$url = 'https://www.flow.cl/api';
// Agrega a la url el servicio a consumir
$url = $url . '/payment/create';
//Agrega la firma a los parámetros
$params["s"] = $signature;
try {
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  curl_setopt($ch, CURLOPT_POST, TRUE);
  curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
  $response = curl_exec($ch);
  if($response === false) {
    $error = curl_error($ch);
    throw new Exception($error, 1);
  } 
  $info = curl_getinfo($ch);
  if(!in_array($info['http_code'], array('200', '400', '401')) {
    throw new Exception('Unexpected error occurred. HTTP_CODE: '.$info['http_code'] , $info['http_code']);
  }
  echo $response;
} catch (Exception $e) {
  echo 'Error: ' . $e->getCode() . ' - ' . $e->getMessage();
}
**/

//MAPA

    function iniciarMap(){
    var coord = {lat:-33.363258 ,lng: -70.6798352};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}
