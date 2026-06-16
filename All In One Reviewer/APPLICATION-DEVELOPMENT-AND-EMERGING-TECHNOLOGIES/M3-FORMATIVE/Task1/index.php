<?php
$contacts = [
    [
        "name" => "Zane Anderson",
        "image" => "https://ui-avatars.com/api/?name=Zane+Anderson&background=003366&color=FDFBF7&size=100",
        "age" => 21,
        "birthday" => "March 12, 2005",
        "contact_number" => "09123456789"
    ],
    [
        "name" => "Alice Cooper",
        "image" => "https://ui-avatars.com/api/?name=Alice+Cooper&background=003366&color=FDFBF7&size=100",
        "age" => 20,
        "birthday" => "June 15, 2006",
        "contact_number" => "09234567890"
    ],
    [
        "name" => "Charlie Davis",
        "image" => "https://ui-avatars.com/api/?name=Charlie+Davis&background=003366&color=FDFBF7&size=100",
        "age" => 22,
        "birthday" => "November 3, 2004",
        "contact_number" => "09345678901"
    ],
    [
        "name" => "Bob Baker",
        "image" => "https://ui-avatars.com/api/?name=Bob+Baker&background=003366&color=FDFBF7&size=100",
        "age" => 19,
        "birthday" => "February 22, 2007",
        "contact_number" => "09456789012"
    ],
    [
        "name" => "Yuna Kim",
        "image" => "https://ui-avatars.com/api/?name=Yuna+Kim&background=003366&color=FDFBF7&size=100",
        "age" => 23,
        "birthday" => "September 5, 2003",
        "contact_number" => "09567890123"
    ],
    [
        "name" => "David Evans",
        "image" => "https://ui-avatars.com/api/?name=David+Evans&background=003366&color=FDFBF7&size=100",
        "age" => 20,
        "birthday" => "January 30, 2006",
        "contact_number" => "09678901234"
    ],
    [
        "name" => "Fiona Gallagher",
        "image" => "https://ui-avatars.com/api/?name=Fiona+Gallagher&background=003366&color=FDFBF7&size=100",
        "age" => 21,
        "birthday" => "August 18, 2005",
        "contact_number" => "09789012345"
    ],
    [
        "name" => "Ethan Hunt",
        "image" => "https://ui-avatars.com/api/?name=Ethan+Hunt&background=003366&color=FDFBF7&size=100",
        "age" => 22,
        "birthday" => "July 9, 2004",
        "contact_number" => "09890123456"
    ],
    [
        "name" => "Hannah Irving",
        "image" => "https://ui-avatars.com/api/?name=Hannah+Irving&background=003366&color=FDFBF7&size=100",
        "age" => 19,
        "birthday" => "December 12, 2007",
        "contact_number" => "09901234567"
    ],
    [
        "name" => "George Harris",
        "image" => "https://ui-avatars.com/api/?name=George+Harris&background=003366&color=FDFBF7&size=100",
        "age" => 24,
        "birthday" => "April 25, 2002",
        "contact_number" => "09012345678"
    ]
];

usort($contacts, function($a, $b) {
    return strcasecmp($a['name'], $b['name']);
});
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task 1: Alphabetical Student Directory</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #FDFBF7; 
            color: #003366; 
            margin: 0;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            color: #003366;
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* Table Styling matching your image */
        table {
            width: 100%;
            max-width: 1000px;
            border-collapse: collapse;
            background-color: #ffffff; 
            box-shadow: 0 4px 8px rgba(0, 51, 102, 0.1); 
        }

        th, td {
            border: 2px solid #003366; 
            padding: 15px;
            text-align: center;
            vertical-align: middle;
        }

        th {
            background-color: #003366; 
            color: #FDFBF7; 
            text-transform: capitalize;
            font-weight: 600;
            font-size: 1.1rem;
        }

        td {
            font-size: 1rem;
        }

        .profile-img {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #003366;
        }

        tbody tr:nth-child(even) {
            background-color: #F4F1EA; 
        }
        
        tbody tr:hover {
            background-color: #E8E2D2; 
        }
    </style>
</head>
<body>

    <h1>Contact Directory</h1>

    <table>
        <thead>
            <tr>
                <th>no.</th>
                <th>name</th>
                <th>Image</th>
                <th>age</th>
                <th>birthday</th>
                <th>contact number</th>
            </tr>
        </thead>
        <tbody>
            <?php 
            $counter = 1; 
            foreach ($contacts as $person): 
            ?>
                <tr>
                    <td><?php echo $counter; ?></td>
                    <td><?php echo htmlspecialchars($person['name']); ?></td>
                    <td>
                        <img class="profile-img" src="<?php echo htmlspecialchars($person['image']); ?>" alt="<?php echo htmlspecialchars($person['name']); ?>">
                    </td>
                    <td><?php echo htmlspecialchars($person['age']); ?></td>
                    <td><?php echo htmlspecialchars($person['birthday']); ?></td>
                    <td><?php echo htmlspecialchars($person['contact_number']); ?></td>
                </tr>
            <?php 
            $counter++; 
            endforeach; 
            ?>
        </tbody>
    </table>

</body>
</html>