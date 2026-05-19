<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>String Functions Table</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table {
            width: 100%;
            border-collapse: collapse;
            text-align: center;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
        }
        th { background-color: #ddd; }
    </style>
</head>
<body>

<h2>Task 2: PHP String Functions</h2>

<table>
    <tr>
        <th>Name</th>
        <th>Number of characters</th>
        <th>Uppercase first</th>
        <th>Replace vowels with @</th>
        <th>Check position of character "a"</th>
        <th>Reverse name</th>
    </tr>

    <?php
    $names = [
        "chrisa", "dawn", "andrei", "carlos", "diana",
        "elijah", "fiona", "gabriel", "hannah", "isaac",
        "julia", "kevin", "luna", "mateo", "nora",
        "oliver", "penelope", "quinn", "ryan", "stella"
    ];

    $vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

    foreach ($names as $name) {
        $length = strlen($name);
        $ucFirst = ucfirst($name);
        $replacedVowels = str_replace($vowels, '@', $name);

        $pos = strpos(strtolower($name), 'a');
        $position = ($pos !== false) ? $pos : "None"; 
        
        $reversed = strrev($name);

        echo "<tr>
                <td>{$name}</td>
                <td>{$length}</td>
                <td>{$ucFirst}</td>
                <td>{$replacedVowels}</td>
                <td>{$position}</td>
                <td>{$reversed}</td>
              </tr>";
    }
    ?>
</table>

</body>
</html>