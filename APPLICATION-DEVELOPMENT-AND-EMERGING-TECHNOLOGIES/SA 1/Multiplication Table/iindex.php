<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiplication Table</title>
    <style>
        body {
            font-family: serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 50px;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        table {
            border-collapse: collapse;
            border: 2px solid black;
        }
        td {
            border: 1px solid black;
            width: 40px;
            height: 40px;
            text-align: center;
            vertical-align: middle;
            font-size: 1.2em;
            font-family: sans-serif;
        }
    </style>
</head>
<body>

    <h1>Multiplication Table</h1>

    <table>
        <?php
        // Loop for the rows (0 to 10)
        for ($row = 0; $row <= 10; $row++) {
            echo "<tr>";
            
            // Loop for the columns (0 to 10)
            for ($col = 0; $col <= 10; $col++) {
                
                // Calculate the product
                $product = $row * $col;
                
                // Control structure to determine alternating colors
                // If the sum of row and col is even, make it light blue. Otherwise, green.
                if (($row + $col) % 2 == 0) {
                    $bgColor = "lightblue";
                } else {
                    $bgColor = "lightgreen";
                }
                
                // Output the table data cell with the calculated background color
                echo "<td style='background-color: $bgColor;'>$product</td>";
            }
            
            echo "</tr>";
        }
        ?>
    </table>

</body>
</html>