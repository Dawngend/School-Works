<?php
function calculateMath($param1, $param2, $param3) {
    $sum = $param1 + $param2 + $param3;
    $difference = $param1 - $param2 - $param3;
    $product = $param1 * $param2 * $param3;
    
    if ($param2 != 0 && $param3 != 0) {
        $quotient = $param1 / $param2 / $param3;
    } else {
        $quotient = "Undefined (division by zero)";
    }

    echo '<table>';
    echo '<tbody>';
    echo '<tr>';
    echo '<td colspan="2">My Parameter values: ' . $param1 . ', ' . $param2 . ', ' . $param3 . '</td>';
    echo '</tr>';
    
    echo '<tr>';
    echo '<td>Addition</td>';
    echo '<td>' . $sum . '</td>';
    echo '</tr>';
    
    echo '<tr>';
    echo '<td>Subtraction</td>';
    echo '<td>' . $difference . '</td>';
    echo '</tr>';
    
    echo '<tr>';
    echo '<td>Multiplication</td>';
    echo '<td>' . $product . '</td>';
    echo '</tr>';
    
    echo '<tr>';
    echo '<td>Division</td>';
    echo '<td>' . $quotient . '</td>';
    echo '</tr>';
    
    echo '</tbody>';
    echo '</table>';
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task 3: Parameter Math</title>
    <style>
        body {
            font-family: 'Times New Roman', Times, serif;
            display: flex;
            justify-content: center;
            padding-top: 50px;
            background-color: #ffffff;
            color: #000000;
        }

        table {
            width: 500px;
            border-collapse: collapse;
            border: 3px double #333; 
            text-align: center;
        }

        td {
            border: 1px solid #333; 
            padding: 5px 10px;
            font-size: 1rem;
        }

        td:first-child {
            width: 40%;
        }
    </style>
</head>
<body>

    <?php
        calculateMath(25, 13, 6);
    ?>

</body>
</html>