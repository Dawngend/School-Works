<?php
session_start();
include('db_connect.php');
/** @var mysqli $conn */

if (!isset($_SESSION['username']) || $_SESSION['accesslevel'] !== 'user') {
    header("Location: login.php");
    exit();
}

$error_msg = "";
if (isset($_POST['upload'])) {
    if (isset($_FILES["fileUp"]) && $_FILES["fileUp"]["error"] == UPLOAD_ERR_OK) {
        $target_dir = "uploads/";
        if (!file_exists($target_dir)) { 
            if (!mkdir($target_dir, 0777, true)) {
                $error_msg = "Failed to create uploads directory. Check folder permissions.";
            }
        }

        if (empty($error_msg)) {
            $filename = time() . "_" . basename($_FILES["fileUp"]["name"]); 
            $target_file = $target_dir . $filename;

            if (move_uploaded_file($_FILES["fileUp"]["tmp_name"], $target_file)) { 
                $user_id = $_SESSION['id'];
                $query = "UPDATE tbl_users SET image='$filename' WHERE ID=$user_id"; 
                if (mysqli_query($conn, $query)) { 
                    $_SESSION['image'] = $filename;
                    header("Location: user_home.php");
                    exit();
                } else {
                    $error_msg = "Database update failed: " . mysqli_error($conn);
                }
            } else {
                $error_msg = "Failed to move uploaded file. Check folder permissions.";
            }
        }
    } else {
        $upload_errors = array(
            UPLOAD_ERR_INI_SIZE   => 'The uploaded file exceeds the upload_max_filesize directive in php.ini.',
            UPLOAD_ERR_FORM_SIZE  => 'The uploaded file exceeds the MAX_FILE_SIZE directive that was specified in the HTML form.',
            UPLOAD_ERR_PARTIAL    => 'The uploaded file was only partially uploaded.',
            UPLOAD_ERR_NO_FILE    => 'No file was uploaded.',
            UPLOAD_ERR_NO_TMP_DIR => 'Missing a temporary folder.',
            UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk.',
            UPLOAD_ERR_EXTENSION  => 'A PHP extension stopped the file upload.',
        );
        $code = isset($_FILES["fileUp"]) ? $_FILES["fileUp"]["error"] : UPLOAD_ERR_NO_FILE;
        $error_msg = isset($upload_errors[$code]) ? $upload_errors[$code] : 'Unknown upload error.';
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Upload Image</title>
    <style>
        .container { width: 500px; margin: 20px auto; border: 1px solid black; padding: 20px; border-radius: 8px; font-family: sans-serif; position: relative; }
        .back { position: absolute; top: 20px; right: 20px; }
        .profile-section { display: flex; margin-bottom: 20px; }
        .info { flex: 2; }
        .photo-slot { flex: 1; border: 1px solid #ccc; height: 130px; text-align: center; }
        .photo-slot img { max-width: 100%; max-height: 100%; }
        .upload-section { border-top: 1px solid #ccc; padding-top: 20px; }
        input[type="submit"] { width: 80%; margin: 20px auto 0 auto; display: block; padding: 8px; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; }
        .error { color: red; font-weight: bold; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>My Information</h2>
        <a class="back" href="user_home.php">Back</a>
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
                    <img src="uploads/<?php echo $_SESSION['image']; ?>" alt="Preview">
                <?php endif; ?>
                <div style="font-size:12px;">Preview</div>
            </div>
        </div>

        <div class="upload-section">
            <h3>-Upload Image-</h3>
            <?php if(!empty($error_msg)) { echo "<p class='error'>$error_msg</p>"; } ?>
            <form method="post" action="user_image.php" enctype="multipart/form-data">
                <input type="file" name="fileUp" required>
                <input type="submit" name="upload" value="Upload Image">
            </form>
        </div>
        <div class="footer">© Crix Brix</div>
    </div>
</body>
</html>