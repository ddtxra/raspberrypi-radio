<?php



//    if (isset($_POST['channelUrl'])){

         $radioname = "nrj";
         exec('mpc stop > /dev/null');
         exec('mpc clear > /dev/null');
         exec('mpc add http://217.151.152.245/bigfm-mp3-96 > /dev/null');
         exec('mpc play > /dev/null');

//    }



?>
