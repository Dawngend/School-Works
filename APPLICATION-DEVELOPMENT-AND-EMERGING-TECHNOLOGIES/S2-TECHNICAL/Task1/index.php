<?php
$fruits = [
    "Apple" => [
        "image" => "images/apple.jpg",
        "description" => "Color Red or Green",
        "facts" => "Apples are rich in fiber, vitamins, and antioxidants. They are one of the most widely cultivated tree fruits."
    ],
    "Pineapple" => [
        "image" => "images/pineapple.jpg",
        "description" => "Color Yellow with a Brown rind",
        "facts" => "Pineapples contain bromelain, a group of digestive enzymes that can help break down proteins and aid digestion."
    ],
    "Melon" => [
        "image" => "images/melon.jpg",
        "description" => "Color Green or Orange",
        "facts" => "Melons have a very high water content (often around 90%), making them incredibly hydrating."
    ],
    "Mango" => [
        "image" => "images/mango.jpg",
        "description" => "Color Yellow, Orange, or Red",
        "facts" => "Known as the 'king of fruits,' mangos are rich in beta-carotene and help support eye health."
    ],
    "Blueberry" => [
        "image" => "images/blueberry.jpg",
        "description" => "Color Deep Blue or Purple",
        "facts" => "Blueberries are often considered a superfood due to their extremely high levels of antioxidants, particularly anthocyanins."
    ],
    "Apple Mango" => [
        "image" => "images/apple mango.jpg",
        "description" => "Color Reddish-Yellow",
        "facts" => "This is a specific variety of mango known for its reddish skin that resembles an apple, and it has a notably sweet, rich flavor."
    ],
    "Guyabano" => [
        "image" => "images/guyabano.jpg",
        "description" => "Color Green with a spiky exterior",
        "facts" => "Also known as soursop, it has a creamy texture and a flavor profile often described as a mix of strawberry and pineapple."
    ],
    "Orange" => [
        "image" => "images/orange.jpg",
        "description" => "Color Orange",
        "facts" => "Oranges are a premier source of Vitamin C and also contain good amounts of fiber and potassium."
    ],
    "Avocado" => [
        "image" => "images/avocado.jpg",
        "description" => "Color Dark Green or Black",
        "facts" => "Technically a large berry with a single seed, avocados are unique because they are high in healthy monounsaturated fats rather than carbohydrates."
    ],
    "Strawberry" => [
        "image" => "images/strawberry.jpg",
        "description" => "Color Red",
        "facts" => "Strawberries are the only fruit that wear their seeds on the outside, with an average strawberry containing about 200 seeds."
    ]
];

ksort($fruits);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fruit Directory</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th colspan="4" class="main-title">My Fruits</th>
                </tr>
                <tr>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Facts</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($fruits as $name => $details): ?>
                    <tr>
                        <td class="img-cell"><img src="<?= htmlspecialchars($details['image']) ?>" alt="<?= htmlspecialchars($name) ?>"></td>
                        <td class="name-cell"><?= htmlspecialchars($name) ?></td>
                        <td class="desc-cell"><?= htmlspecialchars($details['description']) ?></td>
                        <td class="facts-cell"><?= htmlspecialchars($details['facts']) ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

</body>
</html>