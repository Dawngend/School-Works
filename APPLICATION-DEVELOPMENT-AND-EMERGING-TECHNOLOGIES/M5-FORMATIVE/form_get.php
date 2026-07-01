<!DOCTYPE html>
<html>
<head>
    <title>Personal Information - GET</title>
</head>
<body>
    <form method="get" action="<?php echo $_SERVER['PHP_SELF'];?>">
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
    if (isset($_GET['submit'])) {
        echo "First Name: " . htmlspecialchars($_GET['fname']) . "<br>";
        echo "Middle Name: " . htmlspecialchars($_GET['mname']) . "<br>";
        echo "Last Name: " . htmlspecialchars($_GET['lname']) . "<br>";
        echo "Date of Birth: " . htmlspecialchars($_GET['dob']) . "<br>";
        echo "Address: " . htmlspecialchars($_GET['address']) . "<br>";
    }
    ?>
</body>
</html>