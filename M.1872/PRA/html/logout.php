<?php
	$conf = $_SERVER['DOCUMENT_ROOT'];
	$conf .= "/conf.php";
	require_once($conf);
	session_destroy();
	header("location: login.php");
?>