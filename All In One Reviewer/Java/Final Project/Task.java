
public class Task {
    //attributes
    private int taskID; //identifier ng task    
    private String description; //desc
    private String assignedTo;  //id of assigned team member
    private String status;  //currect status
    private String priority;    //importance level: priority
    
    public Task(int taskID, String description, String priority) {
        this.taskID = taskID;
        this.description = description;
        this.assignedTo = "Unassigned"; //default
        this.status = "Not Started";    //default
        
        // Validate priority
        if (priority.equals("Low") || priority.equals("Medium") || priority.equals("High")) {
            this.priority = priority;   //
        } else {
            this.priority = "Low";
            System.out.println("Invalid priority. Set to Low.");
        } //validates priority and defaults to "Low" if invalid 
    }
    
    // Getters and Setters
    public int getTaskID() { 
        return taskID; } //getting the taskID identifier
    public void setTaskID(int taskID) { 
        this.taskID = taskID; 
    } //setting the taskID identifier
    

    public String getDescription() { 
        return description; 
    } //getting the task description
    public void setDescription(String description) { 
        this.description = description; 
    } //setting task description
    
    public String getAssignedTo() { 
        return assignedTo; 
    } //assigned team member's id
    public void setAssignedTo(String assignedTo) { 
        this.assignedTo = assignedTo; 
    } //setting team member's id
    
    public String getStatus() { 
        return status; 
    } //
    public void setStatus(String status) { //setting status
        if (status.equals("Not Started") || status.equals("In Progress") || status.equals("Completed")) {
            this.status = status;
        } else { //if invalid
            System.out.println("Invalid status. Use: Not Started, In Progress, or Completed");
        }
    }
    
    public String getPriority() { 
        return priority; 
    } //priotity of task
    public void setPriority(String priority) { 
        if (priority.equals("Low") || priority.equals("Medium") || priority.equals("High")) {
            this.priority = priority;
        }
    } //setting priority of tasks
    
    @Override
    public String toString() {
        return taskID + "," + description + "," + assignedTo + "," + status + "," + priority;
    }
}   //converts task inputs to string format for file handling
    