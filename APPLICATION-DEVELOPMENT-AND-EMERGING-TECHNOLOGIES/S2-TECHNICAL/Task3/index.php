<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Resume</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="resume-container">
        
        <div class="top-section">
            <div class="profile-pic">
                <img src="images/profile.jpg" alt="Profile Picture">
            </div>
            <div class="personal-info">
                <?php require 'includes/personal_info.php'; ?>
            </div>
        </div>

        <div class="section">
            <?php include 'includes/objective.php'; ?>
        </div>

        <div class="section">
            <?php include 'includes/education.php'; ?>
        </div>

        <div class="section">
            <?php include 'includes/skills.php'; ?>
        </div>

        <div class="section">
            <?php include 'includes/affiliations.php'; ?>
        </div>

        <div class="section">
            <?php include 'includes/experience.php'; ?>
        </div>

    </div>
</body>
</html>