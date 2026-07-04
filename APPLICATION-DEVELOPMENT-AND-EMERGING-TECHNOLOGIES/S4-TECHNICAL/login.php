<?php
session_start();
include('db_connect.php');
/** @var mysqli $conn */

if (isset($_GET['action']) && $_GET['action'] == 'logout') {
    session_unset();
    session_destroy();
    // Restart session just to show a clean login form state if needed
    session_start();
}

$error_msg = "";

if (isset($_POST['login'])) {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = $_POST['password']; // In production, use password_verify() with password_hash()

    $query = "SELECT * FROM tbl_users WHERE username='$username' AND password='$password'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) == 1) {
        $user = mysqli_fetch_assoc($result);
        
        if ($user['status'] == 'disable') {
            $error_msg = "This account is disabled please contact the administrator"; 
        } else {
            $_SESSION['id'] = $user['ID'];
            $_SESSION['username'] = $user['username'];
            $_SESSION['accesslevel'] = $user['accesslevel'];
            $_SESSION['firstname'] = $user['Firstname'];
            $_SESSION['lastname'] = $user['Lastname'];
            $_SESSION['middlename'] = $user['Middlename'];
            $_SESSION['contactno'] = $user['Contactno'];
            $_SESSION['email'] = $user['Email'];
            $_SESSION['birthday'] = $user['Birthday'];
            $_SESSION['image'] = $user['image'];

            if ($user['accesslevel'] == 'admin' || $user['accesslevel'] == 'administrator') {
                header("Location: Admin_home.php");
            } else {
                header("Location: user_home.php");
            }
            exit();
        }
    } else {
        $error_msg = "Invalid Username or Password!";
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        .login-box { width: 300px; margin: 100px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; }
        .error { color: red; font-weight: bold; margin-bottom: 10px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; margin: 10px 0; box-sizing: border-box; }
        input[type="submit"] { width: 100%; padding: 10px; background-color: #e0e0e0; border: 1px solid #999; cursor: pointer; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h3>Log-In Form</h3>
        <?php if(!empty($error_msg)) { echo "<p class='error'>$error_msg</p>"; } ?>
        <form method="post" action="login.php">
            <label>Username</label>
            <input type="text" name="username" required>
            <label>Password</label>
            <input type="password" name="password" required>
            <input type="submit" name="login" value="Login">
        </form>
        <div class="footer">© Crix Brix</div> 
    </div>
</body>
</html>