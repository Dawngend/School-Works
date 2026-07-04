<?php
session_start();
// Security check: Redirect to login if session does not exist
if(!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}
include 'db_connect.php';

$username = $_SESSION['username'];
$message = "";

// Fetch user data
$sql = "SELECT * FROM users WHERE username='$username'";
$result = $conn->query($sql);
$user_data = $result->fetch_assoc();

// Handle Password Reset
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $current = $_POST['current_pw'];
    $new = $_POST['new_pw'];
    $renew = $_POST['renew_pw'];

    if ($current !== $user_data['password']) {
        $message = "<p style='color:red;'>Current password is not the same with the old password</p>";
    } else if ($new !== $renew) {
        $message = "<p style='color:red;'>New password and Re-Enter new password should be the same.</p>";
    } else {
        // Update password in DB
        $update_sql = "UPDATE users SET password='$new' WHERE username='$username'";
        if ($conn->query($update_sql) === TRUE) {
            $message = "<p style='color:green;'>Password reset successfully!</p>";
            // Update local array to reflect change immediately
            $user_data['password'] = $new;
        } else {
            $message = "<p style='color:red;'>Error updating password.</p>";
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>User Information Form</title>
    <style>
        body { font-family: Arial, sans-serif; font-size: 14px; }
        .container { width: 400px; margin: 50px auto; border: 1px solid black; padding: 20px; border-radius: 10px; position: relative;}
        .logout { position: absolute; right: 20px; top: 20px; }
        input[type="password"] { width: 100%; padding: 5px; margin-bottom: 10px; box-sizing: border-box; }
        input[type="submit"] { width: 100%; padding: 5px; cursor: pointer; }
        hr { margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h2>User Information Form</h2>
        <a href="logout.php" class="logout">Log-out</a>
        
        <p><b>Welcome</b> <?php echo $user_data['first_name'] . " " . $user_data['middle_name'] . " " . $user_data['last_name']; ?></p>
        <p><b>Birthday:</b> <?php echo $user_data['birthday']; ?></p>
        <p><b>Contact Details</b></p>
        <ul style="list-style-type:none;">
            <li><b>Email:</b> <?php echo $user_data['email']; ?></li>
            <li><b>Contact:</b> <?php echo $user_data['contact']; ?></li>
        </ul>

        <hr>

        <p>RESET PASSWORD</p>
        <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
            Enter Current Password: <input type="password" name="current_pw" required>
            Enter New Password: <input type="password" name="new_pw" required>
            Re-Enter New Password: <input type="password" name="renew_pw" required>
            <input type="submit" value="Reset Password">
        </form>
        <?php echo $message; ?>
        <p style="text-align:center; font-size:12px; margin-top:20px;">&copy; Crix Brix</p>
    </div>
</body>
</html>