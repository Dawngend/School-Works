
import java.util.ArrayList;

public class TeamMember {
    private String memberID; //unique identifier for team member
    private String memberName; //full name of team member
    private ArrayList<Task> assignedTasks; //list of assigned tasks
    
    public TeamMember(String memberID, String memberName) { //creates a new team member
        this.memberID = memberID;
        this.memberName = memberName;
        this.assignedTasks = new ArrayList<>();
    }
    
    // Getters
    public String getMemberID() { 
        return memberID; 
    } //get member's unique ID
    public String getMemberName() { 
        return memberName; 
    } //get member's full name
    public ArrayList<Task> getAssignedTasks() { 
        return assignedTasks; 
    } // get list of all assigned tasks
    
    public int getInProgressCount() { //counts tasks that are currently "In Progress" for productivity report
        int count = 0;
        for (Task t : assignedTasks) {
            if (t.getStatus().equals("In Progress")) count++;
        }
        return count; //return how many "In Progress" are counted
    }
    
    public void assignTask(Task task) { //implements condition that each team member should only have 5 tasks each max
        if (getInProgressCount() < 5) {
            assignedTasks.add(task);
            task.setAssignedTo(memberID);
            System.out.println("Task assigned successfully to " + memberName);
        } else {
            System.out.println("Cannot assign task. " + memberName + " has 5 tasks in progress.");
        }
    }
    
    public void addTask(Task task) { //assigns a task if they haven't reached max condition
        assignedTasks.add(task);
    }
    
    public boolean canAcceptTask() { //if less than 5 tasks, can accept
        return getInProgressCount() < 5;
    }
    
    public int getCompletedCount() { //getting count of completed tasks for productivity report
        int count = 0;
        for (Task t : assignedTasks) {
            if (t.getStatus().equals("Completed")) count++;
        }
        return count; //return count of "Completed"
    }
    
    public int getPendingCount() { //count "Pending" tasks for productivity report
        return assignedTasks.size() - getCompletedCount();
    }
    
    @Override
    public String toString() { //converts user input into string format for file handling
        StringBuilder sb = new StringBuilder();
        sb.append(memberID).append(",").append(memberName);
        if (!assignedTasks.isEmpty()) {
            sb.append(",");
            for (Task t : assignedTasks) {
                sb.append(t.getTaskID()).append(";");
            }
        }
        return sb.toString();
    }
}