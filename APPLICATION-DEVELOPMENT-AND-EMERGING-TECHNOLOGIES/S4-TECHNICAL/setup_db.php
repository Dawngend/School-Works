<!DOCTYPE html>
<html>
<head>
    <title>Database Setup - Summative 4 Technical</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .setup-box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 500px; text-align: center; border-top: 5px solid #007BFF; }
        h2 { color: #333; margin-bottom: 20px; }
        .status-msg { padding: 12px; border-radius: 4px; margin-bottom: 15px; font-weight: bold; text-align: left; font-size: 14px; }
        .success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .info-box { background-color: #e2e3e5; color: #383d41; border: 1px solid #d6d8db; padding: 15px; border-radius: 4px; text-align: left; margin-top: 20px; }
        .info-box ul { margin: 10px 0 0 0; padding-left: 20px; }
        .btn { display: inline-block; padding: 10px 20px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; margin-top: 20px; transition: background-color 0.2s; }
        .btn:hover { background-color: #0056b3; }
        .log-list { max-height: 150px; overflow-y: auto; text-align: left; background: #272822; color: #f8f8f2; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 12px; }
    </style>
</head>
<body>
    <div class="setup-box">
        <h2>Summative 4 Technical Setup</h2>
        <div class="log-list">
<?php
$servername = "localhost";
$username = "root";
$password = "";

echo "[*] Connecting to MySQL server on '$servername' as '$username'...\n";
// Create connection
$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
    echo "[!] Connection failed: " . mysqli_connect_error() . "\n";
    echo "</div>";
    echo "<div class='status-msg error'>MySQL Connection Failed! Please check if your MySQL server (like XAMPP/WAMP) is running and the credentials in setup_db.php/db_connect.php are correct.</div>";
    exit();
}
echo "[+] Connected successfully to MySQL server.\n";

// Create database if not exists
$dbname = "lab_assessment";
$sql = "CREATE DATABASE IF NOT EXISTS $dbname";
if (mysqli_query($conn, $sql)) {
    echo "[+] Database '$dbname' verified/created successfully.\n";
} else {
    echo "[!] Error creating database: " . mysqli_error($conn) . "\n";
    echo "</div>";
    echo "<div class='status-msg error'>Error creating database.</div>";
    exit();
}

// Select the database
if (mysqli_select_db($conn, $dbname)) {
    echo "[+] Selected database '$dbname'.\n";
} else {
    echo "[!] Error selecting database: " . mysqli_error($conn) . "\n";
    echo "</div>";
    echo "<div class='status-msg error'>Error selecting database.</div>";
    exit();
}

// Create table tbl_users if not exists
$table_sql = "CREATE TABLE IF NOT EXISTS tbl_users (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Firstname VARCHAR(50) NOT NULL,
    Middlename VARCHAR(50) DEFAULT NULL,
    Lastname VARCHAR(50) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    Birthday DATE DEFAULT NULL,
    Email VARCHAR(100) DEFAULT NULL,
    Contactno VARCHAR(20) DEFAULT NULL,
    accesslevel VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    image VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;";

if (mysqli_query($conn, $table_sql)) {
    echo "[+] Table 'tbl_users' verified/created successfully.\n";
} else {
    echo "[!] Error creating table: " . mysqli_error($conn) . "\n";
    echo "</div>";
    echo "<div class='status-msg error'>Error creating table.</div>";
    exit();
}

// Create uploads directory if not exists
$target_dir = "uploads/";
if (!file_exists($target_dir)) {
    if (mkdir($target_dir, 0777, true)) {
        echo "[+] Uploads directory created.\n";
    } else {
        echo "[!] Warning: Could not create uploads directory.\n";
    }
} else {
    echo "[+] Uploads directory exists.\n";
}

// Insert default users if table is empty
$count_query = "SELECT COUNT(*) as total FROM tbl_users";
$res = mysqli_query($conn, $count_query);
$row = mysqli_fetch_assoc($res);

if ($row['total'] == 0) {
    echo "[*] Table is empty. Seeding 5 default accounts...\n";
    
    // Account 1: Admin
    $insert_1 = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status) 
                 VALUES ('Admin', 'System', 'User', 'admin', 'admin', '1990-01-01', 'admin@example.com', '1234567890', 'admin', 'active')";
    
    // Account 2: Active User 1
    $insert_2 = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status) 
                 VALUES ('Alice', 'Marie', 'Smith', 'user1', 'user1', '1995-05-15', 'alice@example.com', '09171234567', 'user', 'active')";
                 
    // Account 3: Active User 2
    $insert_3 = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status) 
                 VALUES ('Bob', 'Lee', 'Johnson', 'user2', 'user2', '1997-08-20', 'bob@example.com', '09187654321', 'user', 'active')";
                 
    // Account 4: Disabled User (to test disabled validation)
    $insert_4 = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status) 
                 VALUES ('Charlie', 'Brown', 'Davis', 'user3', 'user3', '1994-03-12', 'charlie@example.com', '09191112222', 'user', 'disable')";
                 
    // Account 5: Active User 3
    $insert_5 = "INSERT INTO tbl_users (Firstname, Middlename, Lastname, username, password, Birthday, Email, Contactno, accesslevel, status) 
                 VALUES ('Diana', 'Prince', 'Wayne', 'user4', 'user4', '1992-10-31', 'diana@example.com', '09203334444', 'user', 'active')";
    
    if (mysqli_query($conn, $insert_1) && mysqli_query($conn, $insert_2) && mysqli_query($conn, $insert_3) && mysqli_query($conn, $insert_4) && mysqli_query($conn, $insert_5)) {
        echo "[+] 5 default accounts seeded successfully!\n";
    } else {
        echo "[!] Error seeding default accounts: " . mysqli_error($conn) . "\n";
    }
} else {
    echo "[+] Accounts already exist in 'tbl_users'. Seeding skipped.\n";
}

mysqli_close($conn);
?>
        </div>
        
        <div class="status-msg success">
            Setup Completed Successfully! The database and tables are ready to use.
        </div>
        
        <div class="info-box">
            <strong>Default Credentials:</strong>
            <ul>
                <li><strong>Admin Account:</strong> Username: <code>admin</code> | Password: <code>admin</code> (Access: Admin panel)</li>
                <li><strong>User Account 1:</strong> Username: <code>user1</code> | Password: <code>user1</code> (Access: User panel)</li>
                <li><strong>User Account 2:</strong> Username: <code>user2</code> | Password: <code>user2</code> (Access: User panel)</li>
                <li><strong>User Account 3 (Disabled):</strong> Username: <code>user3</code> | Password: <code>user3</code> (Test: Disabled error message)</li>
                <li><strong>User Account 4:</strong> Username: <code>user4</code> | Password: <code>user4</code> (Access: User panel)</li>
            </ul>
        </div>
        
        <a href="login.php" class="btn">Go to Login Page</a>
    </div>
</body>
</html>
