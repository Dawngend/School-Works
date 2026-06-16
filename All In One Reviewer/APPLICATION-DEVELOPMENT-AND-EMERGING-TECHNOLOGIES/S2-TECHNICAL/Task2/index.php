<?php
// 1. User Defined Functions for Volume Calculations
function getVolumeCube($s) {
    return pow($s, 3);
}

function getVolumeRectangularPrism($l, $w, $h) {
    return $l * $w * $h;
}

function getVolumeCylinder($r, $h) {
    return round(pi() * pow($r, 2) * $h, 2); 
}

function getVolumeCone($r, $h) {
    return round((1/3) * pi() * pow($r, 2) * $h, 2);
}

function getVolumeSphere($r) {
    return round((4/3) * pi() * pow($r, 3), 2);
}

$cube_s = 5;
$rect_l = 4; $rect_w = 3; $rect_h = 5;
$cyl_r = 4; $cyl_h = 10;
$cone_r = 3; $cone_h = 7;
$sph_r = 6;
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volume of Shapes</title>
    <link rel="stylesheet" href="css/task2-style.css">
</head>
<body>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th colspan="3" class="main-title">Volume of Shapes</th>
                </tr>
                <tr class="sub-header">
                    <th>Values</th>
                    <th>Formula</th>
                    <th>Answer</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>s = <?= $cube_s ?></td>
                    <td>V = s<sup>3</sup></td>
                    <td><?= getVolumeCube($cube_s) ?></td>
                </tr>
                <tr>
                    <td>l = <?= $rect_l ?>, w = <?= $rect_w ?>, h = <?= $rect_h ?></td>
                    <td>V = l &times; w &times; h</td>
                    <td><?= getVolumeRectangularPrism($rect_l, $rect_w, $rect_h) ?></td>
                </tr>
                <tr>
                    <td>r = <?= $cyl_r ?>, h = <?= $cyl_h ?></td>
                    <td>V = &pi;r<sup>2</sup>h</td>
                    <td><?= getVolumeCylinder($cyl_r, $cyl_h) ?></td>
                </tr>
                <tr>
                    <td>r = <?= $cone_r ?>, h = <?= $cone_h ?></td>
                    <td>V = <sup>1</sup>&frasl;<sub>3</sub>&pi;r<sup>2</sup>h</td>
                    <td><?= getVolumeCone($cone_r, $cone_h) ?></td>
                </tr>
                <tr>
                    <td>r = <?= $sph_r ?></td>
                    <td>V = <sup>4</sup>&frasl;<sub>3</sub>&pi;r<sup>3</sup></td>
                    <td><?= getVolumeSphere($sph_r) ?></td>
                </tr>
            </tbody>
        </table>
    </div>

</body>
</html>