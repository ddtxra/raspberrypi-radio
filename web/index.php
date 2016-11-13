<?php
    
    if (isset($_POST['button_off'])) {     exec('piradio off');}
    if (isset($_POST['button_minus'])) {     exec('piradio vol - ');}
    if (isset($_POST['button_plus'])) {     exec('piradio vol + ');}

    if (isset($_POST['button_nrj']))
    {
         $radioname = "nrj";
         exec('piradio ' . $radioname);
    }



	if (isset($_POST['button_nrj']))
    {
	 $radioname = "nrj";
         exec('piradio ' . $radioname);
    }

       if (isset($_POST['button_kiz']))
    {
         $radioname = "kizomba";
         exec('piradio ' . $radioname);
    }

       if (isset($_POST['button_rtl']))
    {
         $radioname = "rtl";
         exec('piradio ' . $radioname);
    }
?>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<style>
button {
    margin: 30px;
}
h1 {
  text-align: center;
}
</style>

<body>
    <h1>PortuLiana Radio</h1>
    <div class="container">

    <form method="post">
    <p>
	<div class="row">

	<div>
        	<button class="col-md-12 btn btn-danger" name="button_off">Turn Off</button>
	</div>

	<div>
        	<button class="col-md-5 btn btn-success" name="button_minus">Vol -</button>
        	<button class="col-md-5 btn btn-success" name="button_plus">Vol +</button>
        </div>

	<div> <button class="col-md-12 btn btn-primary" name="button_nrj" value="nrj">Listen to NRJ</button> </div>
        <div> <button class="col-md-12 btn btn-primary" name="button_kiz" value="kizomba">Listen to Kizomba</button> </div>
        <div> <button class="col-md-12 btn btn-primary" name="button_rtl" value="RTL 102.5">Listen to RTL</button> </div>
	
	</div>

    </p>
    </form> 

   </div>
</body>
