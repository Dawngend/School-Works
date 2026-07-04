<?php
session_start();
include('db_connect.php');
/** @var mysqli $conn */

if (!isset($_SESSION['username']) || $_SESSION['accesslevel'] !== 'user') {
    header("Location: login.php");
    exit();
}

$msg = "";
if (isset($_POST['submit'])) {
    $current = $_POST['current_password'];
    $new = $_POST['new_password'];
    $confirm = $_POST['confirm_password'];
    $user_id = $_SESSION['id'];

    $check_query = "SELECT password FROM tbl_users WHERE ID=$user_id";
    $res = mysqli_query($conn, $check_query);
    $row = mysqli_fetch_assoc($res);

    if ($row['password'] === $current) {
        if ($new === $confirm) {
            $update_query = "UPDATE tbl_users SET password='$new' WHERE ID=$user_id";
            if (mysqli_query($conn, $update_query)) {
                $msg = "<span style='color:green;'>Password changed successfully!</span>";
            }
        } else { $msg = "<span style='color:red;'>New passwords do not match!</span>"; }
    } else { $msg = "<span style='color:red;'>Incorrect current password!</span>"; }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
    <style>
        .container { width: 500px; margin: 20px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; position: relative; }
        .back { position: absolute; top: 20px; right: 20px; }
        .form-section { border-top: 1px solid #ccc; padding-top: 20px; margin-top: 20px; }
        .form-group { display: flex; margin: 8px 0; align-items: center; }
        .form-group label { width: 180px; }
        .form-group input { flex: 1; padding: 4px; }
        input[type="submit"] { width: 80%; margin: 20px auto 0 auto; display: block; padding: 8px; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>My Information</h2>
        <a class="back" href="user_home.php">Back</a>
        <p><b>Welcome</b> <?php echo $_SESSION['firstname'] . " " . $_SESSION['lastname']; ?></p> 
        <p><b>Userlevel:</b> <?php echo $_SESSION['accesslevel']; ?></p>
        <p><b>Birthday:</b> <?php echo $_SESSION['birthday']; ?></p>
        <div class="form-section">
            <h3>-Password Reset-</h3>
            <?php echo $msg; ?>
            <form method="post" action="user_changepass.php">
                <div class="form-group"><label>Enter Current Password:</label><input type="password" name="current_password" required></div> 
                <div class="form-group"><label>Enter New Password:</label><input type="password" name="new_password" required></div> 
                <div class="form-group"><label>Re-Enter New Password:</label><input type="password" name="confirm_password" required></div> 
                <input type="submit" name="submit" value="Submit">
            </form>
        </div>
        <div class="footer">© Crix Brix</div>
    </div>
</body>
</html>