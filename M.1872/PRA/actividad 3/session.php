<?php
	$conf = $_SERVER['DOCUMENT_ROOT'];
	$conf .= "/conf.php";
	require_once($conf);
	session_start();
	$user_check = $_SESSION['email'];

	if(!isset($_SESSION['email'])){
		header("location:login.php");
	}
?>