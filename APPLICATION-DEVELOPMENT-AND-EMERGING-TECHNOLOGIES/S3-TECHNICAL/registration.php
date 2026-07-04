<?php
session_start();
if(isset($_SESSION['username'])) {
    header("Location: home.php");
    exit();
}
include 'db_connect.php';
$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fname = $_POST['fname'];
    $mname = $_POST['mname'];
    $lname = $_POST['lname'];
    $user = $_POST['username'];
    $pass = $_POST['password'];
    $cpass = $_POST['cpassword'];
    $bday = $_POST['birthday'];
    $email = $_POST['email'];
    $contact = $_POST['contact'];

    if ($pass !== $cpass) {
        $message = "<p style='color:red;'>password and confirm password are not the same</p>";
    } else {
        $sql = "INSERT INTO users (first_name, middle_name, last_name, username, password, birthday, email, contact) 
                VALUES ('$fname', '$mname', '$lname', '$user', '$pass', '$bday', '$email', '$contact')";

        if ($conn->query($sql) === TRUE) {
            $message = "<div style='margin-top:20px;'>
                        Full Name: $fname $mname $lname <br>
                        Username: $user <br>
                        Password: $pass <br>
                        Birthday: $bday <br>
                        Email: $email <br>
                        Contact Number: $contact
                        </div>";
        } else {
            $message = "Error: " . $conn->error;
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Registration</title>
    <style>
        body { font-family: Arial, sans-serif; font-size: 14px; }
        .container { width: 300px; margin: 20px auto; }
        input[type="text"], input[type="password"] { width: 100%; padding: 5px; margin-bottom: 10px; box-sizing: border-box; }
        input[type="submit"] { width: 100%; padding: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <p>My Personal Information</p>
        <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
            First Name<br><input type="text" name="fname" required>
            Middle Name<br><input type="text" name="mname" required>
            Last Name<br><input type="text" name="lname" required>
            Username<br><input type="text" name="username" required>
            Password<br><input type="password" name="password" required>
            Confirm Password<br><input type="password" name="cpassword" required>
            Birthday<br><input type="text" name="birthday" required>
            Email<br><input type="text" name="email" required>
            Contact Number<br><input type="text" name="contact" required>
            <input type="submit" value="Submit">
        </form>
        <p style="font-size:12px;">&copy; Dawn Pamesa</p>
        
        <?php echo $message; ?>
        <br>
        <a href="login.php">Go to Login</a>
    </div>
</body>
</html>