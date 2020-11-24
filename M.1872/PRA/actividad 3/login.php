<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
	<head>
		<meta charset="utf-8">
		<?php
			$conf = $_SERVER['DOCUMENT_ROOT'];
			$conf .= '/conf.php';
			require_once ($conf);
		?>
	</head>
	<body>
		<?php
			$message = '';
			if (isset ($_POST["login"])) {
				$query = 'SELECT * FROM Users WHERE Email = :user_email;';
				$statement = $connect->prepare ($query);
				$statement->execute (
					array (
						'user_email'	=>	$_POST['user_email']
					)
				);
				$count = $statement->rowCount ();
				if ($count > 0) {
					$result = $statement->fetchAll ();
					foreach ($result as $row) {
						if ($row['Password'] == $_POST['user_password']) {
							$_SESSION['email'] = $_POST['user_email'];
							header ('location: index.php');
						} else $message = 'Wrong username or password';
					}
				} else $message = 'Wrong username or password';
			} else $message = 'Please login first';
		?>
		<form id = "Login" method = "post">
			<?php echo $message;?>
			<br>
			Email<input type = "email" name = "user_email"/>
			Password<input type = "password" name = "user_password"/>
			<button typ = "submit" name = "login">Login</button>
		</form>
	</body>
</html>