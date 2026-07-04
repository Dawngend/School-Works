<?php
session_start();
include('db_connect.php');
/** @var mysqli $conn */

if (!isset($_SESSION['username']) || ($_SESSION['accesslevel'] !== 'admin' && $_SESSION['accesslevel'] !== 'administrator')) {
    header("Location: login.php");
    exit();
}

$query = "SELECT * FROM tbl_users"; 
$records = mysqli_query($conn, $query);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Admin Home</title>
    <style>
        .container { width: 800px; margin: 20px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; position: relative; }
        .logout { position: absolute; top: 20px; right: 20px; }
        .profile-section { display: flex; margin-bottom: 20px; }
        .info { flex: 2; }
        .photo-slot { flex: 1; border: 1px solid #ccc; height: 150px; display: flex; align-items: center; justify-content: center; }
        .photo-slot img { max-width: 100%; max-height: 100%; }
        .links { margin: 20px 0; border-top: 1px solid #ccc; padding-top: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 13px; }
        th, td { border: 1px solid black; padding: 6px; text-align: left; }
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
            <a href="Admin_image.php">upload image</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="Admin_changepass.php">Reset my password</a> 
        </div>

        <h3>-Records-</h3> 
        <a href="Admin_adduser.php">Add New User</a> 
        <table>
            <tr>
                <th>ID</th><th>First Name</th><th>Middle Name</th><th>Last Name</th>
                <th>Contact No.</th><th>Email</th><th>Birthday</th><th>Username</th>
                <th>Access Level</th><th>Status</th>
            </tr>
            <?php while($row = mysqli_fetch_assoc($records)): ?> 
            <tr>
                <td><?php echo $row['ID']; ?></td>
                <td><?php echo $row['Firstname']; ?></td>
                <td><?php echo $row['Middlename']; ?></td>
                <td><?php echo $row['Lastname']; ?></td>
                <td><?php echo $row['Contactno']; ?></td>
                <td><?php echo $row['Email']; ?></td>
                <td><?php echo $row['Birthday']; ?></td>
                <td><?php echo $row['username']; ?></td>
                <td><?php echo $row['accesslevel']; ?></td>
                <td><span style="color: blue;"><?php echo $row['status']; ?></span></td>
            </tr>
            <?php endwhile; ?>
        </table>
        <div class="footer">© Crix Brix</div> 
    </div>
</body>
</html>