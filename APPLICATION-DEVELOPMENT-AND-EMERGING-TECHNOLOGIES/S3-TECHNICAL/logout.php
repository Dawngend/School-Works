<?php
session_start();
session_unset();
session_destroy();

// Optional: Delete cookies upon logout by setting expiration to the past
setcookie("user_cookie", "", time() - 3600, "/");
setcookie("pass_cookie", "", time() - 3600, "/");

header("Location: login.php");
exit();
?>