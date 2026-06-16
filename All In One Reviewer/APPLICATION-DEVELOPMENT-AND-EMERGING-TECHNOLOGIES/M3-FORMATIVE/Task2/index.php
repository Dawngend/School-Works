<?php
$numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


$sum = array_sum($numbers);

$difference = $numbers[0];
for ($i = 1; $i < count($numbers); $i++) {
    $difference -= $numbers[$i];
}

$product = array_product($numbers);

$quotient = $numbers[0];
for ($i = 1; $i < count($numbers); $i++) {
    $quotient /= $numbers[$i];
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task 2: Array Math Operations</title>
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
            width: 600px;
            border-collapse: collapse;
            border: 3px double #333; 
            text-align: center;
        }

        td {
            border: 1px solid #333;
            padding: 8px 15px;
            font-size: 1.1rem;
        }

        td:first-child {
            width: 40%;
        }
    </style>
</head>
<body>

    <table>
        <tbody>
            <tr>
                <td colspan="2">Array list: <?php echo implode(', ', $numbers); ?></td>
            </tr>
            <tr>
                <td>Addition</td>
                <td><?php echo $sum; ?></td>
            </tr>
            <tr>
                <td>Subtraction</td>
                <td><?php echo $difference; ?></td>
            </tr>
            <tr>
                <td>Multiplication</td>
                <td><?php echo $product; ?></td>
            </tr>
            <tr>
                <td>Division</td>
                <td><?php echo $quotient; ?></td> 
            </tr>
        </tbody>
    </table>

</body>
</html>