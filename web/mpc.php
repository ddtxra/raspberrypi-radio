<?php

  $_POST = json_decode(file_get_contents('php://input'), true);

  function turnOffRadio ($off) {
    if(strcmp($off,"off") == 0){  exec('piradio off'); echo "Turning off radio"; }
  }

  function changeVolume ($volume) {
    if(strcmp($volume,"plus") == 0){  exec('piradio vol +'); echo "Changing volume to plus"; }
    else if(strcmp($volume,"minus") == 0){  exec('piradio vol -'); echo "Changing volume to minus";  }
  }

  function changeChannel ($channel) {

    exec('mpc stop > /dev/null');
    exec('mpc clear > /dev/null');
    exec('mpc add ' . $channel . ' > /dev/null');
    exec('mpc play > /dev/null');

    echo "Changing channel to " + $channel;

  }

  //Checking parameters
  if(isset($_POST['volume'])){  changeVolume($_POST['volume']); } 
  else if(isset($_POST['channel'])) { changeChannel($_POST['channel']);  }
  else if(isset($_POST['off'])) { turnOffRadio($_POST['off']);  }

?>
