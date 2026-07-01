<?php
// Start the session
session_start();

// Store POST data into Session variables if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $_SESSION["color1"] = $_POST['color1'];
    $_SESSION["color2"] = $_POST['color2'];
    $_SESSION["color3"] = $_POST['color3'];
    $_SESSION["color4"] = $_POST['color4'];
    $_SESSION["color5"] = $_POST['color5'];
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Result Colors</title>
</head>
<body>
    <?php
    // Check if session variables are set, then output
    if(isset($_SESSION["color1"])) {
        echo "My Favorite Color 1: " . htmlspecialchars($_SESSION["color1"]) . "<br>";
        echo "My Favorite Color 2: " . htmlspecialchars($_SESSION["color2"]) . "<br>";
        echo "My Favorite Color 3: " . htmlspecialchars($_SESSION["color3"]) . "<br>";
        echo "My Favorite Color 4: " . htmlspecialchars($_SESSION["color4"]) . "<br>";
        echo "My Favorite Color 5: " . htmlspecialchars($_SESSION["color5"]) . "<br>";
    } else {
        echo "No session data found. Please submit the form first.";
    }
    ?>
</body>
</html>