<?php
session_start();
if (!isset($_SESSION['username']) || $_SESSION['accesslevel'] !== 'user') {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>User Home</title>
    <style>
        .container { width: 600px; margin: 40px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; position: relative; }
        .logout { position: absolute; top: 20px; right: 20px; }
        .profile-section { display: flex; margin-bottom: 20px; }
        .info { flex: 2; }
        .photo-slot { flex: 1; border: 1px solid #ccc; height: 150px; display: flex; align-items: center; justify-content: center; }
        .photo-slot img { max-width: 100%; max-height: 100%; }
        .links { margin: 20px 0; border-top: 1px solid #ccc; padding-top: 10px; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>My Information</h2> 
        <a class="logout" href="login.php?action=logout">Logout</a> 
        
        <div class="profile-section">
            <div class="info">
                <p><b>Welcome</b> <?php echo $_SESSION['firstname'] . " " . $_SESSION['lastname']; ?></p> 
                <p><b>Userlevel:</b> <?php echo $_SESSION['accesslevel']; ?></p> 
                <p><b>Birthday:</b> <?php echo $_SESSION['birthday']; ?></p> 
                <p><b>Contact Details</b></p> 
                <p style="margin-left:20px;"><b>Contact:</b> <?php echo $_SESSION['contactno']; ?></p> 
                <p style="margin-left:20px;"><b>Email:</b> <?php echo $_SESSION['email']; ?></p> 
            </div>
            <div class="photo-slot">
                <?php if(!empty($_SESSION['image'])): ?>
                    <img src="uploads/<?php echo $_SESSION['image']; ?>" alt="Profile">
                <?php else: ?>
                    <span style="color:#aaa;">No Image</span>
                <?php endif; ?>
            </div>
        </div>

        <div class="links">
            <a href="user_image.php">upload image</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="user_changepass.php">Reset my password</a> 
        </div>
        <div class="footer">© Crix Brix</div> 
    </div>
</body>
</html>