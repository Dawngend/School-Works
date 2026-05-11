<?php
// Initialize variables
$isSubmitted = false;
$formattedLastName = $formattedFirstName = $formattedMiddleName = "";
$gender = $formattedDob = $formattedPrevSchool = $formattedMedical = $formattedCountry = "";
$formattedGuardianName = $guardianRelation = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $isSubmitted = true;

    // 1. Convert user entries into variables
    $rawLastName = $_POST['lastName'] ?? '';
    $rawFirstName = $_POST['firstName'] ?? '';
    $rawMiddleName = $_POST['middleName'] ?? '';
    $gender = $_POST['gender'] ?? 'Not Specified';
    
    $dobYear = $_POST['dobYear'] ?? '';
    $dobMonth = $_POST['dobMonth'] ?? '';
    $dobDay = $_POST['dobDay'] ?? '';

    $rawPrevSchool = $_POST['prevSchool'] ?? '';
    $rawMedical = $_POST['medicalConditions'] ?? 'None';
    $rawCountry = $_POST['country'] ?? '';
    
    // Guardian Data
    $rawGuardianName = $_POST['guardianName'] ?? '';
    $guardianRelation = $_POST['guardianRelation'] ?? '';

    // 2. String and Number Formatting
    $formattedLastName = ucwords(strtolower(trim($rawLastName)));
    $formattedFirstName = ucwords(strtolower(trim($rawFirstName)));
    $formattedMiddleName = ucwords(strtolower(trim($rawMiddleName)));
    $formattedPrevSchool = ucwords(strtolower(trim($rawPrevSchool)));
    $formattedGuardianName = ucwords(strtolower(trim($rawGuardianName)));
    
    $formattedMedical = ucfirst(strtolower(trim($rawMedical)));
    $formattedCountry = strtoupper(trim($rawCountry));

    $formattedMonth = str_pad($dobMonth, 2, "0", STR_PAD_LEFT);
    $formattedDay = str_pad($dobDay, 2, "0", STR_PAD_LEFT);
    $formattedDob = "$dobYear-$formattedMonth-$formattedDay";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration Form</title>
    <style>
        body { background-color: #FDFBF7; font-family: Arial, sans-serif; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 850px; margin: 0 auto; background-color: #FAF5E9; padding: 30px; border-top: 8px solid #004080; border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1, h2 { color: #004080; }
        h1 { text-align: right; border-bottom: 2px solid #004080; padding-bottom: 10px; }
        .section-title { background-color: #333; color: white; padding: 5px 10px; font-size: 14px; text-transform: uppercase; margin-top: 20px; margin-bottom: 15px; }
        .row { display: flex; gap: 15px; margin-bottom: 15px; }
        .col { flex: 1; }
        label { display: block; font-size: 12px; margin-bottom: 5px; color: #555; }
        input[type="text"], input[type="number"], select { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 3px; }
        .submit-btn { background-color: #004080; color: white; padding: 12px 25px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; margin-top: 20px; }
        .submit-btn:hover { background-color: #00264d; }
        .output-box { margin-top: 30px; background-color: #E6F0FA; border: 2px dashed #004080; padding: 20px; border-radius: 5px; }
        .highlight { font-weight: bold; color: #004080; }
    </style>
</head>
<body>

<div class="container">
    <h1>Student Registration Form</h1>

    <form method="POST" action="">
        <div class="section-title">Student Information</div>
        <div class="row">
            <div class="col">
                <input type="text" name="lastName" required>
                <label>Last Name</label>
            </div>
            <div class="col">
                <input type="text" name="firstName" required>
                <label>First Name</label>
            </div>
            <div class="col">
                <input type="text" name="middleName">
                <label>Middle Name</label>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <label>Gender:</label>
                <input type="radio" name="gender" value="Male" required> Male
                <input type="radio" name="gender" value="Female" required> Female
            </div>
            <div class="col row">
                <div class="col"><input type="number" name="dobYear" placeholder="YYYY" required><label>Year</label></div>
                <div class="col"><input type="number" name="dobMonth" placeholder="MM" required min="1" max="12"><label>Month</label></div>
                <div class="col"><input type="number" name="dobDay" placeholder="DD" required min="1" max="31"><label>Day</label></div>
            </div>
        </div>

        <div class="section-title">Guardian Information</div>
        <div class="row">
            <div class="col">
                <label>Full Name of Guardian:</label>
                <input type="text" name="guardianName" required>
            </div>
            <div class="col">
                <label>Relationship to Student:</label>
                <select name="guardianRelation" required>
                    <option value="">Select Relation</option>
                    <option value="Father">Father</option>
                    <option value="Mother">Mother</option>
                    <option value="Legal Guardian">Legal Guardian</option>
                    <option value="Grandparent">Grandparent</option>
                    <option value="Other">Other</option>
                </select>
            </div>
        </div>

        <div class="section-title">Previous School & Health</div>
        <div class="row">
            <div class="col">
                <label>Name of Previous School:</label>
                <input type="text" name="prevSchool">
            </div>
        </div>
        <div class="row">
            <div class="col">
                <label>Medical Conditions:</label>
                <input type="text" name="medicalConditions">
            </div>
        </div>

        <div class="section-title">Citizenship Information</div>
        <div class="row">
            <div class="col">
                <label>Country of Citizenship:</label>
                <input type="text" name="country" required>
            </div>
        </div>

        <button type="submit" class="submit-btn">Submit Registration</button>
    </form>

    <?php if ($isSubmitted): ?>
        <div class="output-box">
            <h2>Registration Successful</h2>
            <p><strong>Student Name:</strong> <span class="highlight"><?php echo "$formattedLastName, $formattedFirstName $formattedMiddleName"; ?></span></p>
            <p><strong>Gender:</strong> <span class="highlight"><?php echo $gender; ?></span></p>
            <p><strong>Date of Birth:</strong> <span class="highlight"><?php echo $formattedDob; ?></span></p>
            <p><strong>Guardian:</strong> <span class="highlight"><?php echo $formattedGuardianName; ?></span> (<?php echo $guardianRelation; ?>)</p>
            <p><strong>Previous School:</strong> <span class="highlight"><?php echo $formattedPrevSchool; ?></span></p>
            <p><strong>Medical Conditions:</strong> <span class="highlight"><?php echo $formattedMedical; ?></span></p>
            <p><strong>Country of Citizenship:</strong> <span class="highlight"><?php echo $formattedCountry; ?></span></p>
        </div>
    <?php endif; ?>
</div>

</body>
</html>