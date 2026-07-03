<?php
session_start();
if(isset($_SESSION['username'])) {
    header("Location: home.php");
    exit();
}
include 'db_connect.php';
$error = "";

// Check for cookies to pre-fill the form
$saved_user = isset($_COOKIE['user_cookie']) ? $_COOKIE['user_cookie'] : "";
$saved_pass = isset($_COOKIE['pass_cookie']) ? $_COOKIE['pass_cookie'] : "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Set Session
        $_SESSION['username'] = $user;

        // Set Cookies if Remember Me is checked
        if(isset($_POST['remember'])) {
            setcookie("user_cookie", $user, time() + (86400 * 30), "/"); 
            setcookie("pass_cookie", $pass, time() + (86400 * 30), "/"); 
        }

        header("Location: home.php");
        exit();
    } else {
        $error = "Invalid username or password.";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; font-size: 14px; }
        .container { width: 300px; margin: 50px auto; border: 1px solid black; padding: 20px; border-radius: 5px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 5px; margin-bottom: 10px; box-sizing: border-box; }
        input[type="submit"] { width: 100%; padding: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h3>Log-In Form</h3>
        <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
            Username<br>
            <input type="text" name="username" value="<?php echo $saved_user; ?>" required>
            Password<br>
            <input type="password" name="password" value="<?php echo $saved_pass; ?>" required>
            <br>
            <input type="checkbox" name="remember"> Remember Me <br><br>
            <input type="submit" value="Login">
        </form>
        <p style="color:red; text-align:center;"><?php echo $error; ?></p>
        <p style="text-align:center; font-size:12px;">&copy; Dawn Pamesa</p>
        <a href="registration.php">Register Here</a>
    </div>
</body>
</html>