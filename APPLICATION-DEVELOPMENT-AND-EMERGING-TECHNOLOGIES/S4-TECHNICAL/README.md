# Summative 4 Technical - User Management System

A PHP and MySQL-based user management system that allows administrators to add and manage users, reset passwords, and upload profile pictures, while regular users can view their information, change passwords, and upload profile pictures.

## Prerequisites

To run this application, you need to have a local PHP and MySQL development environment. The easiest way is to use **XAMPP**:
1. Download and install [XAMPP](https://www.apachefriends.org/index.html) (includes Apache web server and MySQL database).

---

## Installation & Setup Instructions

Follow these steps to run the project locally:

### 1. Copy Files to XAMPP Directory
Copy the entire `S4-TECHNICAL` folder and paste it into the XAMPP `htdocs` directory:
- **Default Path:** `C:\xampp\htdocs\`
- **Resulting Path:** `C:\xampp\htdocs\S4-TECHNICAL\`

### 2. Start Servers
1. Open the **XAMPP Control Panel**.
2. Click **Start** for both **Apache** and **MySQL**.

### 3. Initialize the Database
1. Open your web browser and navigate to:
   [http://localhost/S4-TECHNICAL/setup_db.php](http://localhost/localhost/S4-TECHNICAL/setup_db.php)
2. This script will automatically:
   - Create the `lab_assessment` database.
   - Create the `tbl_users` table.
   - Seed default **Administrator** and **User** accounts.
   - Create the `uploads/` directory for profile picture storage.

### 4. Open the Web Application
Once setup is complete, you can access the login page at:
[http://localhost/S4-TECHNICAL/login.php](http://localhost/S4-TECHNICAL/login.php)

---

## Default Login Credentials

Use the following default accounts to log in:

### 1. Administrator Account
- **Username:** `admin`
- **Password:** `admin`
- **Access Level:** `admin` (Can see all user records, add new users, reset own password, upload own image)

### 2. Standard User Account
- **Username:** `user`
- **Password:** `user`
- **Access Level:** `user` (Can see own details, reset own password, upload own image)

---

## File Structure

- [db_connect.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/db_connect.php) - Establishes the database connection.
- [setup_db.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/setup_db.php) - Automated database initialization and seeding script.
- [login.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/login.php) - Login form, credential validation, and log out session handler.
- [Admin_home.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/Admin_home.php) - Home dashboard for Admin users showing table records.
- [Admin_adduser.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/Admin_adduser.php) - Form for Admins to add new standard users.
- [Admin_changepass.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/Admin_changepass.php) - Password reset page for Admins.
- [Admin_image.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/Admin_image.php) - Profile picture upload page for Admins.
- [user_home.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/user_home.php) - Home dashboard for standard users.
- [user_changepass.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/user_changepass.php) - Password reset page for standard users.
- [user_image.php](file:///D:/School-Works/APPLICATION-DEVELOPMENT-AND-EMERGING-TECHNOLOGIES/S4-TECHNICAL/user_image.php) - Profile picture upload page for standard users.
