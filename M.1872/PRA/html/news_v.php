<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta charset="utf-8">
		<?php
			$conf = $_SERVER['DOCUMENT_ROOT'];
			$conf .= "/conf.php";
			require_once ($conf);
		?>
	</head>
	<body style = 'font-family:verdana; margin: 0px;'>
	<div style = 'display: flex; background-color: #000000; height: 10px;'></div>
		<div style = 'display: flex; justify-content: flex-end; padding-top: 20px;'>
			<div style = 'margin-right: 20px;'>
				<button style = 'padding: 5px; border: none;' onclick = 'notEnabled()'>Register</button>&nbsp;&nbsp;&nbsp;
				<?php
					if (!isset ($_SESSION["email"])) {
						echo '<button style = \'padding: 5px; border: none;\' onclick = \'login()\'>Log in</button>';
					} else {
						echo '<button style = \'padding: 5px; border: none;\' onclick = \'logout()\'>Log out</button>';
					}
				?>
			</div>
		</div>
		<div style = 'display: flex; justify-content: flex-end;'>
			<div style = 'margin-right: 20px;'>
				<h2><a href='index.php' style = 'color: #aaaaaa; text-decoration:none; padding-right: 30px;'>Home</a><a href='#' style = 'color: #aaaaaa; text-decoration:none; padding-right: 30px;'>About</a><a href='#' style = 'color: #aaaaaa; text-decoration:none;'>Contact</a></h2>
			</div>
		</div>
		<div style = 'display: flex; background-color: #dddddd;'>
			<h1>Noticias</h1>
		</div>
		<div style = 'display: flex; background-color: #dddddd;'>
		<div style = 'margin-left: 25px; padding-left: 25px; width: 50px; height: 30px; 0px; background: #ffffff; -moz-border-radius: 0px 0px 100px 100px; -webkit-border-radius: 0px 0px 100px 100px; border-radius: 0px 0px 100px 100px;'></div>
		</div>
		<?php
			if (isset($_GET['id'])) {
				$query = 'SELECT Title, Body, Datetime FROM News WHERE id='.$_GET['id'].';';
				$statement = $connect->prepare ($query);
				$statement->execute ();
				$row = $statement->fetch ();
				$title = $row[0];
				$body = $row[1];
				$datetime = strtotime ($row[2]);
			}
        ?>
		<div style = 'display: flex; background-color: #dddddd;'>
			<div style = 'margin-left: 20px;'>
				<?php echo '<h2>'.$title.'</h2>';?>
			</div>
		</div>
		<div style = 'display: flex; background-color: #dddddd;'>
			<div style = 'margin-left: 20px;'>
				<?php echo '<h4>'.date('d/m/Y h:i:s', $datetime).'</h4>';?>
			</div>
		</div>
		<div style = 'display: flex; background-color: #dddddd;'>
			<div style = 'margin-left: 20px;padding-bottom: 25px;'>
				<?php echo $body;?>
			</div>
		</div>
		<div style = 'display: flex; background-color: #cccccc; height: 10px'></div>
	</body>
	<script>
		function notEnabled() {
			alert("Disabled");
		}
		function logout() {
			window.location.href = "logout.php";
		}
		function login() {
			window.location.href = "login.php";
		}
	</script>
</html>