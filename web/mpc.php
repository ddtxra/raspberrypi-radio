<?php

  $_POST = json_decode(file_get_contents('php://input'), true);


  $radioname = $_POST['channelUrl'];
  echo "Asking to change for " .  $radioname;
  
  exec('mpc stop > /dev/null');
  exec('mpc clear > /dev/null');
  exec('mpc add ' . $radioname . ' > /dev/null');
  exec('mpc play > /dev/null');

?>
