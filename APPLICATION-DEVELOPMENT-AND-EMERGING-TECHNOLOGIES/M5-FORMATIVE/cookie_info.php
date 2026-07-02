<?php
// Setting cookies to expire after 10, 20, and 30 seconds respectively
setcookie("firstname", "Chris", time() + 10, "/");
setcookie("middlename", "Rosales", time() + 20, "/");
setcookie("lastname", "Tio", time() + 30, "/");
?>
<!DOCTYPE html>
<html>
<head>
    <title>Cookie Display</title>
</head>
<body>
    <h3>Current Cookies Stored:</h3>
    <?php
    if(count($_COOKIE) > 0) {
        echo "<pre>";
        print_r($_COOKIE);
        echo "</pre>";
    } else {
        echo "No cookies are currently set or they have expired.";
    }
    ?>
    <p><em>Refresh the page after 10, 20, and 30 seconds to see the cookies expire and disappear one by one.</em></p>
</body>
</html>