
import java.io.*;
import java.util.*;

public class ProjectManager {
    private String managerID; //unique identifier for manager
    private String managerName; //mgr full name
    private ArrayList<Task> tasks;  //all tasks in the system. Use for privilege to assign tasks
    private ArrayList<TeamMember> teamMembers;  //all team members in the system. to be able to assign tasks to
    private HashMap<Integer, Task> taskMap; //ability to lookup tasks by just using ID 
    
    public ProjectManager(String managerID, String managerName) { //creates new project manager and loads existing data
        this.managerID = managerID;
        this.managerName = managerName;
        this.tasks = new ArrayList<>(); //initialize empty task list
        this.teamMembers = new ArrayList<>(); //initialize empty team member list
        this.taskMap = new HashMap<>(); //initialize empty task map for quick lookup
        loadData(); //load existing data from files
    }
    
    // Getters
    public String getManagerID() { 
        return managerID; //get mgr's unique ID
    }
    public String getManagerName() { 
        return managerName; //get mgr's name
    }
    public ArrayList<Task> getTasks() { 
        return tasks; //get list of all tasks in the system
    }
    public ArrayList<TeamMember> getTeamMembers() { 
        return teamMembers; //get list of all team members in the system
    }
    public HashMap<Integer, Task> getTaskMap() { 
        return taskMap; //get to lookup tasks by just inputting their unique ID
    }
    
    public void addTask(Task task) { //add task to the system
        if (taskMap.containsKey(task.getTaskID())) { //checks if there's duplicate. Looks up in taskMap
            System.out.println("Task ID already exists!"); //error message for duplicate ID
            return;
        }
        tasks.add(task); //add to tasks list
        taskMap.put(task.getTaskID(), task); //add to task map for quick lookup
        System.out.println("Task added successfully!"); //success message
    } //if no duplicate found, will successfully add task
    
    public void addTeamMember(TeamMember member) {
        teamMembers.add(member); //for adding a team member to the system
    }
    
    public boolean assignTask(int taskID, String memberID) { //assigning tasks to a team member with validation
        Task task = taskMap.get(taskID); //look up task by ID
        if (task == null) {
            System.out.println("Task not found!"); //check if taskID does indeed exist. If not, then not found
            return false;
        }
        
        TeamMember member = getMemberByID(memberID); //find team member by ID
        if (member == null) {
            System.out.println("Team member not found!"); //check if the team member exists in the program
            return false;
        }
        
        if (!member.canAcceptTask()) { //check if the specific team member hasn't reached the max condition of 5 tasks
            System.out.println("Cannot assign task. Team member already has 5 tasks in progress!"); //if already reached 5, cannot assign tasks
            return false;
        }
        
        member.assignTask(task); //assign task to member
        return true; //if member exists and not yet reached maximum condition, then assign task to member successfully
    }
    
    public void updateTaskStatus(int taskID, String newStatus) { //updates a task's status
        Task task = taskMap.get(taskID); //checking in taskMap for the task
        if (task != null) {
            task.setStatus(newStatus); //update status of task if found in the system
            System.out.println("Task status updated successfully!"); //success message
        } else {
            System.out.println("Task not found!"); //error message if specific task cannot be found in the system
        }
    }
    
    public void viewAllTasks() { //view all tasks in the system
        if (tasks.isEmpty()) {
            System.out.println("No tasks available."); //error message if no tasks yet available
            return;
        }
        
        System.out.println("\n=== ALL TASKS ==="); //print all tasks in formatted table
        System.out.printf("%-10s %-30s %-15s %-15s %-10s\n", 
            "Task ID", "Description", "Assigned To", "Status", "Priority"); //table headers
        System.out.println("------------------------------------------------------------------------"); //table separator
        
        for (Task task : tasks) { //getting output for all tasks in the system from the tasks list
            System.out.printf("%-10d %-30s %-15s %-15s %-10s\n",
                task.getTaskID(), //task ID
                task.getDescription(), //task description
                task.getAssignedTo(), //assigned team member
                task.getStatus(), //current status
                task.getPriority()); //priority level
        } //formatted output for each task
    }
    
    public void generateProductivityReport() { //generation of productivity report for all team members in the system
        System.out.println("\n=== PRODUCTIVITY REPORT ==="); //report header
        System.out.printf("%-15s %-20s %-15s %-15s\n", 
            "Member ID", "Member Name", "Completed", "Pending"); //report headers
        System.out.println("--------------------------------------------------"); //report separator
        
        for (TeamMember member : teamMembers) { //getting output for each team member's data
            System.out.printf("%-15s %-20s %-15d %-15d\n",
                member.getMemberID(), //member ID
                member.getMemberName(), //member name
                member.getCompletedCount(), //completed tasks count
                member.getPendingCount()); //pending tasks count
        } //formatted output for each team member's productivity
    }
    
    private TeamMember getMemberByID(String id) { //finds a team member by inputting their unique memberID
        for (TeamMember member : teamMembers) {
            if (member.getMemberID().equals(id)) {
                return member; //performs linear search through teamMember list
            }
        }
        return null; //return null if team member not found in the system
    }
    
    public void saveData() { //file handling part - save data to files
        // Save tasks to tasks.txt
        try (PrintWriter writer = new PrintWriter(new FileWriter("tasks.txt"))) {
            for (Task task : tasks) {
                writer.println(task.toString()); //saves all tasks using toString format
            }
            System.out.println("Tasks saved successfully to tasks.txt!"); //success message for task saving
        } catch (IOException e) {
            System.out.println("Error saving tasks: " + e.getMessage()); //catch message in case task cannot be saved in txt file
        } //saving all tasks in the entire system in "tasks.txt"
        
        // Save team members to teamMembers.txt
        try (PrintWriter writer = new PrintWriter(new FileWriter("teamMembers.txt"))) {
            for (TeamMember member : teamMembers) {
                writer.println(member.toString()); //saves all team members using toString format
            }
            System.out.println("Team members saved successfully to teamMembers.txt!"); //success message for team member saving
        } catch (IOException e) {
            System.out.println("Error saving team members: " + e.getMessage()); //catch message in case team member cannot be saved in txt file
        } //saving all team members in the entire system in "teamMembers.txt"
    }
    
    private void loadData() { //loading data from text files when program starts
        // Load tasks from tasks.txt
        try (BufferedReader reader = new BufferedReader(new FileReader("tasks.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) { //read each line from file
                String[] parts = line.split(","); //split line by commas
                if (parts.length == 5) { //ensure proper format
                    int taskID = Integer.parseInt(parts[0]); //parse task ID
                    String description = parts[1]; //get description
                    String assignedTo = parts[2]; //get assigned team member
                    String status = parts[3]; //get status
                    String priority = parts[4]; //get priority
                    
                    Task task = new Task(taskID, description, priority); //create new task
                    task.setAssignedTo(assignedTo); //set assignment
                    task.setStatus(status); //set status
                    
                    tasks.add(task); //add to tasks list
                    taskMap.put(taskID, task); //add to task map
                }
            } //basically reads the data in the .txt files then parses each line into Task objects
            System.out.println("Tasks loaded successfully from tasks.txt!"); //success message
        } catch (IOException e) {
            System.out.println("No existing task data found or error reading tasks.txt"); //catch message if error reading .txt file or no data to be outputted
        }
        
        // Load team members from teamMembers.txt - FIXED VERSION
        try (BufferedReader reader = new BufferedReader(new FileReader("teamMembers.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) { //read each line from file
                String[] parts = line.split(","); //split line by commas
                if (parts.length >= 2) { //ensure basic member info exists
                    String memberID = parts[0]; //get member ID
                    String memberName = parts[1]; //get member name
                    
                    //this method allows only load team members that belong to this specific manager
                    if (belongsToThisManager(memberID)) {
                        TeamMember member = new TeamMember(memberID, memberName); //create new team member
                        
                        // Load assigned tasks if available
                        if (parts.length > 2 && !parts[2].isEmpty()) { //check if member has assigned tasks
                            String[] taskIDs = parts[2].split(";"); //split task IDs
                            for (String taskIDStr : taskIDs) {
                                if (!taskIDStr.isEmpty()) { //skip empty strings
                                    try {
                                        int taskID = Integer.parseInt(taskIDStr); //parse task ID
                                        Task task = taskMap.get(taskID); //find task in task map
                                        if (task != null) {
                                            member.addTask(task); //assign task to member
                                        }
                                    } catch (NumberFormatException e) {
                                        System.out.println("Invalid task ID format: " + taskIDStr); //error for invalid task ID
                                    }
                                }
                            }
                        }
                        
                        teamMembers.add(member); //add member to team members list
                    }
                }
            }
            System.out.println("Team members loaded successfully from teamMembers.txt!"); //success message
        } catch (IOException e) {
            System.out.println("No existing team member data found or error reading teamMembers.txt"); //catch message if error reading .txt file or no data
        } //basically reads the data in the .txt files then parses each line into Team Member objects
    }
    
    // Check if a team member belongs to this specific manager
    private boolean belongsToThisManager(String memberID) {
        // Determine which manager owns which team members based on ID ranges
        // PM001 -> TM001, TM002, TM003 (IDs 1-3)
        // PM002 -> TM004, TM005, TM006 (IDs 4-6)  
        // PM003 -> TM007, TM008, TM009 (IDs 7-9)
        
        try {
            int memberNum = Integer.parseInt(memberID.substring(2)); 
            int managerNum = Integer.parseInt(managerID.substring(2)); 
            
            // Calculate the expected member number range for this manager
            int minMemberNum = (managerNum - 1) * 3 + 1; // First member number for this manager
            int maxMemberNum = managerNum * 3; // Last member number for this manager
            
            // Check if member number falls within this manager's range
            return memberNum >= minMemberNum && memberNum <= maxMemberNum;
            
        } catch (NumberFormatException e) {
            return false; // Return false if ID format is invalid
        }
    }
}