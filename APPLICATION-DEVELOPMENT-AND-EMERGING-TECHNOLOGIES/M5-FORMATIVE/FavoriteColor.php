<!DOCTYPE html>
<html>
<head>
    <title>Favorite Colors Input</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 5px;
        }
    </style>
</head>
<body>
    <form method="post" action="ResultColors.php">
        <table>
            <tr>
                <th colspan="2">Enter your favorite colors</th>
            </tr>
            <tr><td>Favorite color 1:</td><td><input type="text" name="color1" value="Red"></td></tr>
            <tr><td>Favorite color 2:</td><td><input type="text" name="color2" value="Yellow"></td></tr>
            <tr><td>Favorite color 3:</td><td><input type="text" name="color3" value="Orange"></td></tr>
            <tr><td>Favorite color 4:</td><td><input type="text" name="color4" value="Violet"></td></tr>
            <tr><td>Favorite color 5:</td><td><input type="text" name="color5" value="Blue"></td></tr>
            <tr><td colspan="2" style="text-align:center;"><input type="submit" value="send colors"></td></tr>
        </table>
    </form>
</body>
</html>