<?php
// Initialize variables
$name = "";
$grade = "";
$rank = "";
$submitted = false;

// Process the form when submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $grade = floatval($_POST['grade']);
    $submitted = true;

    // The Conditional Statement (Grade Ranking Logic)
    if ($grade >= 93 && $grade <= 100) {
        $rank = "A";
    } elseif ($grade >= 90 && $grade < 93) {
        $rank = "A-";
    } elseif ($grade >= 87 && $grade < 90) {
        $rank = "B+";
    } elseif ($grade >= 83 && $grade < 87) {
        $rank = "B";
    } elseif ($grade >= 80 && $grade < 83) {
        $rank = "B-";
    } elseif ($grade >= 77 && $grade < 80) {
        $rank = "C+";
    } elseif ($grade >= 73 && $grade < 77) {
        $rank = "C";
    } elseif ($grade >= 70 && $grade < 73) {
        $rank = "C-";
    } elseif ($grade >= 67 && $grade < 70) {
        $rank = "D+";
    } elseif ($grade >= 63 && $grade < 67) {
        $rank = "D";
    } elseif ($grade >= 60 && $grade < 63) {
        $rank = "D-";
    } else {
        $rank = "F";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade Ranking Program</title>
    <style>
        /* Blue and Cream Colorway */
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

        /* Form Styling */
        .form-container {
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            width: 100%;
            max-width: 400px;
            margin-bottom: 40px;
            border-top: 5px solid var(--blue-primary);
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: var(--blue-primary);
        }

        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 12px;
            background-color: var(--blue-primary);
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: var(--blue-secondary);
        }

        /* Output Card Styling (Mimicking your sample image but better) */
        .result-card {
            background-color: white;
            border: 2px solid var(--blue-primary);
            border-radius: 12px;
            width: 100%;
            max-width: 500px;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }

        .card-left {
            display: flex;
            flex-direction: column;
            flex: 1;
            margin-right: 20px;
        }

        .student-name {
            background-color: var(--cream-card);
            border: 1px solid var(--blue-primary);
            padding: 10px 15px;
            border-radius: 6px;
            font-size: 18px;
            font-weight: bold;
            color: var(--blue-primary);
            margin-bottom: 20px;
        }

        .stats-container {
            display: flex;
            gap: 15px;
        }

        .stat-box {
            background-color: var(--cream-card);
            border: 1px solid var(--blue-primary);
            padding: 15px;
            border-radius: 6px;
            flex: 1;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .stat-label {
            font-size: 14px;
            color: var(--text-dark);
            margin-bottom: 5px;
        }

        .stat-value {
            font-size: 28px;
            font-weight: bold;
            color: var(--blue-primary);
        }

        .card-right {
            width: 130px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .picture-box {
            width: 120px;
            height: 120px;
            background-color: var(--cream-card);
            border: 2px dashed var(--blue-primary);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--blue-primary);
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>

    <!-- Input Form -->
    <div class="form-container">
        <h2 style="color: var(--blue-primary); margin-top: 0;">Grade Evaluator</h2>
        <form method="POST" action="">
            <div class="form-group">
                <label for="name">Student Name</label>
                <input type="text" id="name" name="name" required placeholder="e.g. Dawn Andrei Pamesa">
            </div>
            <div class="form-group">
                <label for="grade">Final Grade (0-100)</label>
                <input type="number" id="grade" name="grade" min="0" max="100" step="0.01" required placeholder="e.g. 92">
            </div>
            <button type="submit">Calculate Rank</button>
        </form>
    </div>

    <!-- Output UI (Only shows after form submission) -->
    <?php if ($submitted): ?>
    <div class="result-card">
        <div class="card-left">
            <div class="student-name">
                Name: <?php echo $name; ?>
            </div>
            
            <div class="stats-container">
                <div class="stat-box">
                    <span class="stat-label">Rank</span>
                    <span class="stat-value"><?php echo $rank; ?></span>
                </div>
                <div class="stat-box">
                    <span class="stat-label">Grade</span>
                    <span class="stat-value"><?php echo number_format($grade, 1); ?></span>
                </div>
            </div>
        </div>
        
        <div class="card-right">
            <div class="picture-box">
                2x2 Picture
            </div>
        </div>
    </div>
    <?php endif; ?>

</body>
</html>