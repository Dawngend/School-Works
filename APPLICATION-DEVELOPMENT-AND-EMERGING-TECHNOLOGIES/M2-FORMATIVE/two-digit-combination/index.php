<?php
/**
 * Activity 3: Two-Digit Decimal Combinations
 * Student: Dawn Andrei Pamesa
 * Institution: FEU Institute of Technology
 */

$combinations = "";
$generated = false;

// Process the form when the button is clicked
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $generated = true;
    
    // The Looping Statement to generate 00 through 99
    for ($i = 0; $i <= 99; $i++) {
        // sprintf("%02d", $i) ensures numbers like '5' become '05'
        $combinations .= sprintf("%02d", $i) . ", ";
    }
    
    // Standard practice: remove the very last comma and space for a clean finish
    $combinations = rtrim($combinations, ", ");
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activity 3: Loop Combinations</title>
    <style>
        /* FEU Tech Project Branding: Blue and Cream Colorway */
        :root {
            --cream-bg: #FDFBF7;
            --cream-card: #F4EFE6;
            --blue-primary: #1E3A8A;
            --blue-secondary: #3B82F6;
            --text-dark: #1F2937;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--cream-bg);
            color: var(--text-dark);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
            margin: 0;
        }

        .container {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
            width: 100%;
            max-width: 700px;
            border-top: 6px solid var(--blue-primary);
            text-align: center;
        }

        h2 {
            color: var(--blue-primary);
            margin-bottom: 10px;
        }

        .description {
            color: #6B7280;
            margin-bottom: 30px;
            font-size: 0.95rem;
        }

        button {
            padding: 14px 40px;
            background-color: var(--blue-primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(30, 58, 138, 0.2);
        }

        button:hover {
            background-color: var(--blue-secondary);
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(59, 130, 246, 0.3);
        }

        /* Output Box Styling (Monospace for better number alignment) */
        .output-container {
            margin-top: 35px;
            text-align: left;
            animation: fadeIn 0.5s ease-in;
        }

        .output-label {
            font-weight: bold;
            color: var(--blue-primary);
            margin-bottom: 10px;
            display: block;
        }

        .output-box {
            background-color: var(--cream-card);
            border: 1px solid #E5E7EB;
            padding: 25px;
            border-radius: 8px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.1rem;
            line-height: 2;
            color: var(--blue-primary);
            word-wrap: break-word;
            border-left: 4px solid var(--blue-primary);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>2-Digit Combination Generator</h2>
        <p class="description">This program uses a <strong>PHP for-loop</strong> to generate all possible decimal combinations from 00 to 99 in a comma-delimited format.</p>
        
        <form method="POST" action="">
            <button type="submit">Generate Decimal Sets</button>
        </form>

        <?php if ($generated): ?>
            <div class="output-container">
                <span class="output-label">Generated Output:</span>
                <div class="output-box">
                    <?php echo htmlspecialchars($combinations); ?>
                </div>
            </div>
        <?php endif; ?>
    </div>

    <footer style="margin-top: 40px; color: #9CA3AF; font-size: 0.8rem;">
        &copy; 2026 Dawn Andrei Pamesa | FEU Tech Emerging Technologies
    </footer>

</body>
</html>