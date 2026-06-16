<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP Length Converter</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 50px; }
        .container { max-width: 500px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { text-align: center; color: #333; }
        label { display: block; margin: 10px 0 5px; }
        input, select { width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background-color: #e9ecef; border-left: 5px solid #28a745; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <h2>Length Converter</h2>
    <form method="POST">
        <label>Enter Length:</label>
        <input type="number" name="value" step="any" required value="<?php echo isset($_POST['value']) ? $_POST['value'] : ''; ?>">

        <label>From:</label>
        <select name="fromUnit">
            <option value="meters">Meters</option>
            <option value="centimeters">Centimeters</option>
            <option value="kilometers">Kilometers</option>
            <option value="inches">Inches</option>
            <option value="feet">Feet</option>
        </select>

        <label>To:</label>
        <select name="toUnit">
            <option value="centimeters">Centimeters</option>
            <option value="meters">Meters</option>
            <option value="kilometers">Kilometers</option>
            <option value="inches">Inches</option>
            <option value="feet">Feet</option>
        </select>

        <button type="submit">Convert</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        require_once 'converters/LengthConverter.php';
        
        $val = floatval($_POST['value']);
        $from = $_POST['fromUnit'];
        $to = $_POST['toUnit'];

        $result = LengthConverter::convert($val, $from, $to);

        echo "<div class='result'>";
        echo "Sample Output: <br>";
        echo "$val $from = " . number_format($result, 2) . " $to";
        echo "</div>";
    }
    ?>
</div>

</body>
</html>