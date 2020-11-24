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
                $collection = $connect->actividad4->users;
                try {
					if ('[$ne]=1' == $_POST['user_password']) $message = 'Injection detected!';
					else {
						$user = $collection->find (array('name'=>filter_var($_POST['user_email'], FILTER_VALIDATE_EMAIL),'password'=>implode($_POST['user_password'])));
						if ($user->count()) {
							$message = 'Login successful!';
						} else $message = 'Username or Password incorrect!';
					}
                } catch (MongoException $e) {
                    die ('Error: '.$e->getMessage());
                }
			} else $message = 'Please login first';
		?>
		<form id = "Login" method = "post">
			<?php echo $message.'<br>';?>
			<br>
			Email<input type = "email" name = "user_email"/>
			Password<input type = "password" name = "user_password"/>
			<button type = "submit" name = "login">Login</button>
		</form>
	</body>
</html>