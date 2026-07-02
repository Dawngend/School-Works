<!DOCTYPE html>
<html>
<head>
    <title>Personal Information - POST</title>
</head>
<body>
    <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
        <table>
            <tr><td>First Name:</td><td><input type="text" name="fname"></td></tr>
            <tr><td>Middle Name:</td><td><input type="text" name="mname"></td></tr>
            <tr><td>Last Name:</td><td><input type="text" name="lname"></td></tr>
            <tr><td>Date of Birth:</td><td><input type="text" name="dob"></td></tr>
            <tr><td>Address:</td><td><input type="text" name="address"></td></tr>
            <tr><td><input type="submit" name="submit" value="Submit"></td><td></td></tr>
        </table>
    </form>
    <br>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['submit'])) {
        echo "First Name: " . htmlspecialchars($_POST['fname']) . "<br>";
        echo "Middle Name: " . htmlspecialchars($_POST['mname']) . "<br>";
        echo "Last Name: " . htmlspecialchars($_POST['lname']) . "<br>";
        echo "Date of Birth: " . htmlspecialchars($_POST['dob']) . "<br>";
        echo "Address: " . htmlspecialchars($_POST['address']) . "<br>";
    }
    ?>
</body>
</html>