<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta charset="utf-8">
		
		<?php
			$conf = $_SERVER['DOCUMENT_ROOT'];
			$conf .= "/conf.php";
			require_once($conf);
			if(!isset($_SESSION["email"])) {
				header("location:login.php");
			}
		?>
		
	</head>
	<body>
		Index
	</body>
</html>