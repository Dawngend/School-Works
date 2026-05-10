<?php
// Make sure this path correctly points to the converter file
require_once '../converters/LengthConverter.php';

// Check if the request is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
    // Read the raw JSON data sent by fetch()
    $json = file_get_contents('php://input');
    $data = json_decode($json, true);

    if ($data) {
        $value = isset($data['inputValue']) ? floatval($data['inputValue']) : 0;
        $fromUnit = isset($data['fromUnit']) ? strtolower($data['fromUnit']) : '';
        $toUnit = isset($data['toUnit']) ? strtolower($data['toUnit']) : '';

        // Call the single unified method
        $result = LengthConverter::convert($value, $fromUnit, $toUnit);

        // Return the JSON response for the JS to read
        if ($result !== null) {
            echo json_encode(['success' => true, 'result' => round($result, 5)]);
        } else {
            echo json_encode(['success' => false]);
        }
    } else {
        echo json_encode(['success' => false]);
    }
}
?>