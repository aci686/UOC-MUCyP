<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta charset="utf-8">
		<?php
			$conf = $_SERVER['DOCUMENT_ROOT'];
			$conf .= "/conf.php";
			require_once ($conf);
			//if (!isset ($_SESSION["email"])) header ("location:login.php");
		?>
	</head>
	<body>
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
        <div  style = 'display: flex; background-color: #dddddd;'>
            <?php
                $query = 'SELECT Id FROM News;';
		    	$statement = $connect->prepare ($query);
		    	$statement->execute ();
		    	$count = $statement->rowCount ();
		    	if ($count > 0) {
		    		$result = $statement->fetchAll ();
		    		foreach ($result as $row) {
                        echo '<a href=news.php?id='.$row['Id'].' style = \'color: #000000; text-decoration:none; font-size: 1.2em;\'>Noticia '.$row['Id'].'</a>';
                    }
                }
            ?>
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
	</body>
</html>