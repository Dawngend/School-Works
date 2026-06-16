<?php
class LengthConverter {
    // Conversion factors relative to 1 Meter
    private static $unitsToMeters = [
        'centimeters' => 0.01,   // 1 cm = 0.01m
        'meters'      => 1,      // Base unit
        'kilometers'  => 1000,   // 1 km = 1000m
        'inches'      => 0.0254, // 1 in = 0.0254m
        'feet'        => 0.3048, // 1 ft = 0.3048m
        'yards'       => 0.9144, // 1 yd = 0.9144m
        'miles'       => 1609.34 // 1 mi = 1609.34m
    ];

    public static function convert($value, $from, $to) {
        if (!isset(self::$unitsToMeters[$from]) || !isset(self::$unitsToMeters[$to])) {
            return "Invalid Unit";
        }

        // Formula: (Input * FromRate) / ToRate
        // First, use the multiplication operator (*) to convert to meters
        $meters = $value * self::$unitsToMeters[$from];
        
        // Second, use the division operator (/) to convert to the target unit
        return $meters / self::$unitsToMeters[$to];
    }
}
?>