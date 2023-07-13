<?php
require_once('Car.php');
require_once("UberX.php");
require_once('Account.php');
require_once("UberPool.php");

$uberX = new UberX("CV123",new Account("Andres Herrera", "AND456"), "Chevrolet","Sparl");

$uberX->PrintDataCar();
echo "hello";
$uberPool = new UberPool("MONH123",new Account("Carla Mendez", "CARL159"), "AUDI","2020");

$uberPool->PrintDataCar();

?>