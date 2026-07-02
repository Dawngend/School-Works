<!DOCTYPE html>
<html>
<head>
    <title>Dog Information Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        .container {
            width: 300px;
        }
        label {
            display: block;
            margin-top: 5px;
        }
        input[type="text"] {
            width: 100%;
            padding: 5px;
            margin-bottom: 5px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            padding: 5px;
            margin-top: 10px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            cursor: pointer;
        }
        .footer {
            margin-top: 5px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php
        // Database connection parameters
        $servername = "localhost";
        $username = "root"; // Default XAMPP username
        $password = "";     // Default XAMPP password
        $dbname = "dog_database";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Process form data when submitted
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $name = $conn->real_escape_string($_POST['d_name']);
            $breed = $conn->real_escape_string($_POST['d_breed']);
            $age = $conn->real_escape_string($_POST['d_age']);
            $address = $conn->real_escape_string($_POST['d_add']);
            $color = $conn->real_escape_string($_POST['d_color']);
            $height = $conn->real_escape_string($_POST['d_height']);
            $weight = $conn->real_escape_string($_POST['d_weight']);

            $sql = "INSERT INTO dog_information (d_name, d_breed, d_age, d_add, d_color, d_height, d_weight) 
                    VALUES ('$name', '$breed', '$age', '$address', '$color', '$height', '$weight')";

            if ($conn->query($sql) === TRUE) {
                echo "<p style='color:green;'>Record saved successfully!</p>";
            } else {
                echo "<p style='color:red;'>Error: " . $conn->error . "</p>";
            }
        }
        $conn->close();
        ?>

        <p>Dog Information</p>
        <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
            <label>Name</label>
            <input type="text" name="d_name" required>
            
            <label>Breed</label>
            <input type="text" name="d_breed" required>
            
            <label>Age</label>
            <input type="text" name="d_age" required>
            
            <label>Address</label>
            <input type="text" name="d_add" required>
            
            <label>Color</label>
            <input type="text" name="d_color" required>
            
            <label>Height</label>
            <input type="text" name="d_height" required>
            
            <label>Weight</label>
            <input type="text" name="d_weight" required>
            
            <input type="submit" value="save">
        </form>
        <div class="footer">&copy; Dawn Pamesa</div>
    </div>
</body>
</html>