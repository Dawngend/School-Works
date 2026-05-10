
import java.util.*;

public class MainProgram {
    private static ArrayList<LogInSystem> loginSystems = new ArrayList<>(); //array containing all login credentials
    private static ArrayList<ProjectManager> projectManagers = new ArrayList<>();   //array containing all project managers
    private static Scanner scanner = new Scanner(System.in);
    private static ProjectManager currentManager = null; //for currently logged-in manager
    private static TeamMember currentMember = null; //for currently logged-in member
    private static String currentUserType = null;   //check role of logged-in user
    
    public static void main(String[] args) {
        initializeData(); //sets up all initial data login credentials
        
        System.out.println("=== TASK MANAGEMENT SYSTEM ==="); //if correct credentials entered. Output this
        
        if (login()) { //check role of user
            if (currentUserType.equals("Project Manager")) { 
                showManagerMenu(); //if manager, show this main menu
            } else {
                showMemberMenu(); //if member, show this menu
            }
        }
     
        
        System.out.println("Thank you for using the Task Management System!");
        scanner.close();
    }
    
    private static void initializeData() {
        // Initialize login credentials
        // Login credentials for Project Managers
        loginSystems.add(new LogInSystem("manager1", "mgrpass1", "Project Manager"));
        loginSystems.add(new LogInSystem("manager2", "mgrpass2", "Project Manager"));
        loginSystems.add(new LogInSystem("manager3", "mgrpass3", "Project Manager"));
        
        // Login credentials for Team Members
        loginSystems.add(new LogInSystem("member1", "pass1", "Team Member"));
        loginSystems.add(new LogInSystem("member2", "pass2", "Team Member"));
        loginSystems.add(new LogInSystem("member3", "pass3", "Team Member"));
        loginSystems.add(new LogInSystem("member4", "pass4", "Team Member"));
        loginSystems.add(new LogInSystem("member5", "pass5", "Team Member"));
        loginSystems.add(new LogInSystem("member6", "pass6", "Team Member"));
        loginSystems.add(new LogInSystem("member7", "pass7", "Team Member"));
        loginSystems.add(new LogInSystem("member8", "pass8", "Team Member"));
        loginSystems.add(new LogInSystem("member9", "pass9", "Team Member"));
        
        // Initialize project managers and their teams
        ProjectManager pm1 = new ProjectManager("PM001", "John Manager");
        ProjectManager pm2 = new ProjectManager("PM002", "Jane Supervisor");
        ProjectManager pm3 = new ProjectManager("PM003", "Bob Director");
        
        // Initialize team members for PM1
        pm1.addTeamMember(new TeamMember("TM001", "Alice Developer"));
        pm1.addTeamMember(new TeamMember("TM002", "Charlie Tester"));
        pm1.addTeamMember(new TeamMember("TM003", "David Analyst"));
        
        // Initialize team members for PM2
        pm2.addTeamMember(new TeamMember("TM004", "Eva Designer"));
        pm2.addTeamMember(new TeamMember("TM005", "Frank Engineer"));
        pm2.addTeamMember(new TeamMember("TM006", "Grace Tester"));
        
        // Initialize team members for PM3
        pm3.addTeamMember(new TeamMember("TM007", "Henry Admin"));
        pm3.addTeamMember(new TeamMember("TM008", "Ivy Support"));
        pm3.addTeamMember(new TeamMember("TM009", "Jack Developer"));
        
        projectManagers.add(pm1);
        projectManagers.add(pm2);
        projectManagers.add(pm3);
    }
    
    private static boolean login() { //handles the authentication process of login credentials
        try {
            System.out.print("Enter username: ");
            String username = scanner.nextLine();
            System.out.print("Enter password: ");
            String password = scanner.nextLine();
            
            System.out.print("Are you a (1) Project Manager or (2) Team Member? ");
            int choice = Integer.parseInt(scanner.nextLine());
            
            if (choice != 1 && choice != 2) {
                System.out.println("Invalid choice! Please enter 1 or 2.");
                return false; //return if invalid choice
            }
            
            String userType = (choice == 1) ? "Project Manager" : "Team Member";
            
            for (LogInSystem login : loginSystems) {
                if (login.verifyLogin(username, password, userType)) {
                    System.out.println("Login successful! Welcome " + userType);
                    currentUserType = userType; //return if correct login credentials entered
                    
                    // Set current manager or member based on login
                    if (userType.equals("Project Manager")) {
                        for (ProjectManager pm : projectManagers) {
                            if (pm.getManagerID().equals("PM00" + username.charAt(username.length()-1))) {
                                currentManager = pm;
                                break;
                            }
                        }
                    } else {
                        // Team Member login
                        for (ProjectManager pm : projectManagers) {
                            for (TeamMember tm : pm.getTeamMembers()) {
                                if (tm.getMemberID().equals("TM00" + username.charAt(username.length()-1))) {
                                    currentMember = tm;
                                    currentManager = pm;
                                    break;
                                }
                            }
                        }
                    }
                    
                    if (currentManager == null) {
                        System.out.println("Error: Could not find user data.");
                        return false;
                    }
                    
                    return true; //basically if the entire login process is true, then return true and load the appropriate main menu for the correct user type if manager or member
                }
            }
            
            System.out.println("Invalid username or password!");
            return false; //if incorrect login credentials. output this error message
            
        } catch (NumberFormatException e) {
            System.out.println("Please enter a valid number!");
            return false; //catch message if invalid number inpputed
        } catch (Exception e) {
            System.out.println("Error during login: " + e.getMessage());
            return false; //catch message if error in login process
        }
    }
    
    private static void showManagerMenu() {
        while (true) {
            System.out.println("\n=== PROJECT MANAGER MENU ===");
            System.out.println("1. Add a new task");
            System.out.println("2. Assign a task to a team member");
            System.out.println("3. Update Task Status");
            System.out.println("4. View all tasks");
            System.out.println("5. Generate Productivity Report");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            
            try {
                int choice = Integer.parseInt(scanner.nextLine()); //read user input then convert it to integer
                
                switch (choice) { //use switch case to handle the different menu choices
                    case 1 -> addNewTask(); 
                    case 2 -> assignTaskToMember(); 
                    case 3 -> updateTaskStatus(); 
                    case 4 -> currentManager.viewAllTasks(); 
                    case 5 -> currentManager.generateProductivityReport();
                    case 6 -> { 
                        currentManager.saveData();
                        System.out.println("======================================\n");
                        return; 
                    } //based on choice. Call the appropriate method based on the choice input number
                    default -> System.out.println("Invalid option! Please try again."); //if choice not valid, then print error message and start again as this is our default output.
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number!"); //catch exception if not valid number
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage()); //catch for error
            }
        } //this is infinite loop until user "Project Manager" picks 6. Exit
    }
    
    private static void showMemberMenu() {
        while (true) {
            System.out.println("\n=== TEAM MEMBER MENU ===");
            System.out.println("1. Update task status");
            System.out.println("2. View all tasks");
            System.out.println("3. Generate productivity report");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            
            
            try {
                int choice = Integer.parseInt(scanner.nextLine()); //read user input then convert it to integer
                
                switch (choice) { //use swithc case to handle the differnt menu choices
                    case 1 -> updateTaskStatusMember();
                    case 2 -> currentManager.viewAllTasks();
                    case 3 -> currentManager.generateProductivityReport();
                    case 4 -> { 
                        currentManager.saveData();
                        System.out.println("======================================\n");
                        return; 
                    } //call appropriate method based on the choice input number by the user
                    default -> System.out.println("Invalid option! Please try again."); //if not valid, print error message as it is our default.
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number!"); //catch exception if not valid number
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage()); //catch exception if error
            }
        } //same as for the manager menu. Infinite loop till user "Team Member" chooses "4. Exit"
    }
    
    private static void addNewTask() {
        try { //this method allows Project Manager to create a new task
            System.out.print("Enter task ID: ");
            int taskID = Integer.parseInt(scanner.nextLine()); //convert into integer
            
            System.out.print("Enter task description: ");
            String description = scanner.nextLine();
            
            System.out.print("Enter priority (Low/Medium/High): ");
            String priority = scanner.nextLine();
            
            //create new task object with the provided user input
            //will handle the dafault values = "Unassigned", status = "Not Started"
            Task newTask = new Task(taskID, description, priority);
            
            //add the new task to the current user "Project Manager" task list
            currentManager.addTask(newTask);
            //the addTask method will check for duplicate ID's and print success/error message if there are duplicates or not
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid task ID format!"); //catch exception if invalid format input
        } catch (Exception e) {
            System.out.println("Error adding task: " + e.getMessage()); //catch exception for any other errors
        }
    }
    
    private static void assignTaskToMember() { //Method that allows Project Manager to assign an existing task to a team member
        try {
            currentManager.viewAllTasks(); //first display all tasks so the manager can know which can be assigned
            System.out.print("Enter task ID to assign: "); //prompt user to which taskID they want to assign
            int taskID = Integer.parseInt(scanner.nextLine()); //convert input into integer
            
            //display all available team members with their current capacity to check if they haven't received max condition
            System.out.println("Available team members:");
            //loop through all the team members that are handled by the specific project manager
            for (TeamMember member : currentManager.getTeamMembers()) {
                //show member details and if they can accept more tasks
                System.out.println(member.getMemberID() + " - " + member.getMemberName() + 
                    " (Can accept task: " + (member.canAcceptTask() ? "Yes" : "No") + ")");
            }
            
            //prompt user which memberID to assign task to
            System.out.print("Enter member ID: ");
            String memberID = scanner.nextLine();
            
            //call the manager assignTask method to perform the actual task
            //validate the assignment of task into the member
            currentManager.assignTask(taskID, memberID);
            //will output sucess/error catch message depending if correct or not
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid task ID format!"); //catch exception if invalid format
        } catch (Exception e) {
            System.out.println("Error assigning task: " + e.getMessage()); //catch exception for other errors
        }
    }
    
    private static void updateTaskStatus() { //this method allows the Project Manager to update the status of any task in the system
        try {
            //display all tasks so manager can see which to update
            currentManager.viewAllTasks();
            
            //prompt user to input specific taskID to update
            System.out.print("Enter task ID to update: ");
            int taskID = Integer.parseInt(scanner.nextLine()); //convert input into integer
            
            //prompt user for new status value
            System.out.print("Enter new status (Not Started/In Progress/Completed): ");
            String newStatus = scanner.nextLine();
            
            //call manager's updateTaskStatus method to perform the update in status
            //a manager has total privilages into updating any task regarding of assignment
            currentManager.updateTaskStatus(taskID, newStatus);
            //the updateTaskStatus will also validate if task exists and status is valid
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid task ID format!"); //catch exception for invalid format
        } catch (Exception e) {
            System.out.println("Error updating task: " + e.getMessage()); //catch exception for any other errors
        }
    }
    
    private static void updateTaskStatusMember() {
        //this allows a team member to update status of their assigned tasks to them
        try {
            //display the tasks assigned only to the specific user "Team Member"
            System.out.println("\nYour assigned tasks:");
            boolean hasTasks = false; //flag to track if member has any tasks
            
            //loop through all tasks in the system
            for (Task task : currentManager.getTasks()) {
                //check if the task is assigned to the specific logged in member
                if (task.getAssignedTo().equals(currentMember.getMemberID())) {
                    //display the task deteals in better formatting
                    System.out.printf("ID: %d, Desc: %s, Status: %s, Priority: %s\n",
                        task.getTaskID(), task.getDescription(), task.getStatus(), task.getPriority());
                    hasTasks = true; //set flag to true since we are able to find at least one task assigned
                }
            }
            
            if (!hasTasks) {
                //if no tasks were found, display the exit message then exit program
                System.out.println("No tasks assigned to you.");
                return;
            }
            
            //prompt user for the specific taskID that they want to update
            //the user can only update the task assigned specifically to them
            System.out.print("Enter task ID to update: ");
            int taskID = Integer.parseInt(scanner.nextLine()); //convert input into integer
            
            //prompt user for new status value
            System.out.print("Enter new status (Not Started/In Progress/Completed): ");
            String newStatus = scanner.nextLine();
            
            //call the manager's updateTaskStatus method to perform the update of status of task
            //we use the manager's update method for consistency and less complications
            currentManager.updateTaskStatus(taskID, newStatus);
            //the method will validate if task exists and if status if valid
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid task ID format!"); //catch exception if invalid format
        } catch (Exception e) {
            System.out.println("Error updating task: " + e.getMessage()); //catch exception for other errors
        }
    }
}