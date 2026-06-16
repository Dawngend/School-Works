
public class LogInSystem {
    private String username; //user's login username
    private String password; //user's password
    private String userType; //check role if "Project Manager" or "Team Member"
    
    public LogInSystem(String username, String password, String userType) { //creates login credentials entry
        this.username = username; //login username
        this.password = password; //login password
        this.userType = userType; //user role type
    }
    
    public boolean verifyLogin(String inputUsername, String inputPassword, String inputUserType) { //verification for login credentials
        return username.equals(inputUsername) && password.equals(inputPassword) && userType.equals(inputUserType);
    } //check if proper and correct login credentials
    
    // Getters
    public String getUsername() { 
        return username; 
    }
    public String getPassword() { 
        return password; 
    }
    public String getUserType() { 
        return userType; 
    }
}