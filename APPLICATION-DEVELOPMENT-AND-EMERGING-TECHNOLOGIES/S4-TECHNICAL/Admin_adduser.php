<?php
session_start();
include('db_connect.php');
/** @var mysqli $conn */

if (!isset($_SESSION['username']) || ($_SESSION['accesslevel'] !== 'admin' && $_SESSION['accesslevel'] !== 'administrator')) {
    header("Location: login.php");
    exit();
}

$error_msg = "";
if (isset($_POST['submit'])) {
    $fname = mysqli_real_escape_string($conn, $_POST['firstname']);
    $mname = mysqli_real_escape_string($conn, $_POST['middlename']);
    $lname = mysqli_real_escape_string($conn, $_POST['lastname']);
    $uname = mysqli_real_escape_string($conn, $_POST['username']);
    $pass  = mysqli_real_escape_string($conn, $_POST['password']);
    $conf_pass = $_POST['confirm_password'];
    $bday  = mysqli_real_escape_string($conn, $_POST['birthday']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $phone = mysqli_real_escape_string($conn, $_POST['contact']);

    if ($pass !== $conf_pass) {
        $error_msg = "Passwords do not match!";
    } else {
        $check_query = "SELECT ID FROM tbl_users WHERE username='$uname'";
        $check_res = mysqli_query($conn, $check_query);
        if (mysqli_num_rows($check_res) > 0) {
            $error_msg = "Username already exists!";
        } else {
            $query = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status)
                        VALUES ('$fname', '$mname', '$lname', '$uname', '$pass', '$bday', '$email', '$phone', 'user', 'active')";
            if (mysqli_query($conn, $query)) {
                header("Location: Admin_home.php");
                exit();
            } else {
                $error_msg = "Error adding user: " . mysqli_error($conn);
            }
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
    <style>
        .container { width: 400px; margin: 40px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; position: relative; }
        .back { position: absolute; top: 20px; right: 20px; }
        .form-group { display: flex; margin: 8px 0; align-items: center; }
        .form-group label { width: 130px; }
        .form-group input { flex: 1; padding: 4px; }
        input[type="submit"] { width: 80%; margin: 20px auto 0 auto; display: block; padding: 8px; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; }
        .error { color: red; font-weight: bold; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Add User</h2> 
        <a class="back" href="Admin_home.php">Back</a> 
        <p>Fill Up Form</p> 
        <?php if(!empty($error_msg)) { echo "<p class='error'>$error_msg</p>"; } ?>
        <form method="post" action="Admin_adduser.php">
            <div class="form-group"><label>First Name:</label><input type="text" name="firstname" required></div> 
            <div class="form-group"><label>Middle Name:</label><input type="text" name="middlename"></div> 
            <div class="form-group"><label>Last Name:</label><input type="text" name="lastname" required></div> 
            <div class="form-group"><label>Username:</label><input type="text" name="username" required></div> 
            <div class="form-group"><label>Password:</label><input type="password" name="password" required></div> 
            <div class="form-group"><label>Confirm Password:</label><input type="password" name="confirm_password" required></div> 
            <div class="form-group"><label>Birthday:</label><input type="text" name="birthday" placeholder="YYYY-MM-DD"></div> 
            <div class="form-group"><label>Email:</label><input type="email" name="email"></div> 
            <div class="form-group"><label>Contact Number:</label><input type="text" name="contact"></div> 
            <input type="submit" name="submit" value="Submit">
        </form>
        <div class="footer">© Crix Brix</div>
    </div>
</body>
</html>