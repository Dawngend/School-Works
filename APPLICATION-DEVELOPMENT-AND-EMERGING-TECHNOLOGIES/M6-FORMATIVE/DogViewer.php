<!DOCTYPE html>
<html>
<head>
    <title>View Dog Records</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        .dog-card {
            border: 1px solid black;
            padding: 10px;
            margin-bottom: 10px;
            width: 350px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <?php
    // Database connection parameters
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "dog_database";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Select all records from the table
    $sql = "SELECT * FROM dog_information";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $counter = 1;
        // Output data of each row
        while($row = $result->fetch_assoc()) {
            echo "<div class='dog-card'>";
            echo "Dog " . $counter . "<br>";
            echo "Name: " . htmlspecialchars($row["d_name"]) . "<br>";
            echo "Breed: " . htmlspecialchars($row["d_breed"]) . "<br>";
            echo "Age: " . htmlspecialchars($row["d_age"]) . "<br>";
            echo "Address: " . htmlspecialchars($row["d_add"]) . "<br>";
            echo "Color: " . htmlspecialchars($row["d_color"]) . "<br>";
            echo "Height: " . htmlspecialchars($row["d_height"]) . "<br>";
            echo "Weight: " . htmlspecialchars($row["d_weight"]) . "<br>";
            echo "</div>";
            $counter++;
        }
    } else {
        echo "0 results found.";
    }
    
    $conn->close();
    ?>
</body>
</html>