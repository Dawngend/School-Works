package attendancetracker;
import java.io.*;
import java.util.*;
import java.time.*;

class ATTENDANCERECORD {
    private String DATE;
    private boolean ISPRESENT;

    public ATTENDANCERECORD(String DATE, boolean ISPRESENT) {
        this.DATE = DATE;
        this.ISPRESENT = ISPRESENT;
    }

    public String GETDATE() { return DATE; }
    public boolean ISPRESENT() { return ISPRESENT; }
    public void SETPRESENT(boolean status) { this.ISPRESENT = status; }

    @Override
    public String toString() { return DATE + "," + ISPRESENT; }

    public static ATTENDANCERECORD FROMSTRING(String line) {
        if (line == null || line.trim().isEmpty()) throw new IllegalArgumentException("Empty attendance record");
        String[] parts = line.split(",");
        if (parts.length != 2) throw new IllegalArgumentException("Invalid attendance record: " + line);
        String date = parts[0].trim();
        boolean present = Boolean.parseBoolean(parts[1].trim());
        return new ATTENDANCERECORD(date, present);
    }
}

class EMPLOYEE {
    private int EMPLOYEEID;
    private String NAME;
    private double SALARYPERDAY;
    private List<ATTENDANCERECORD> ATTENDANCERECORDS;

    public EMPLOYEE(int EMPLOYEEID, String NAME, double SALARYPERDAY) {
        this.EMPLOYEEID = EMPLOYEEID;
        this.NAME = NAME;
        this.SALARYPERDAY = SALARYPERDAY;
        this.ATTENDANCERECORDS = new ArrayList<>();
    }

    public int GETEMPLOYEEID() { return EMPLOYEEID; }
    public String GETNAME() { return NAME; }
    public double GETSALARYPERDAY() { return SALARYPERDAY; }
    public List<ATTENDANCERECORD> GETATTENDANCERECORDS() { return ATTENDANCERECORDS; }

    public void MARK_ATTENDANCE(String date, boolean isPresent) {
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) {
            if (record.GETDATE().equals(date)) {
                System.out.println("Attendance for this date already marked!");
                return;
            }
        }
        ATTENDANCERECORDS.add(new ATTENDANCERECORD(date, isPresent));
        System.out.println("Attendance marked successfully for " + date);
    }

    public void UPDATE_ATTENDANCE(String date, boolean isPresent) {
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) {
            if (record.GETDATE().equals(date)) {
                record.SETPRESENT(isPresent);
                System.out.println("Attendance updated successfully for " + date);
                return;
            }
        }
        System.out.println("No record found for this date: " + date);
    }

    public void RESET_ALL_ATTENDANCE() {
        ATTENDANCERECORDS.clear();
        System.out.println("All attendance records have been reset.");
    }

    public void RESET_ATTENDANCE_BY_MONTH(int month, int year) {
        ATTENDANCERECORDS.removeIf(r -> {
            LocalDate d = LocalDate.parse(r.GETDATE());
            return d.getMonthValue() == month && d.getYear() == year;
        });
        System.out.println("Attendance records for " + year + "-" + String.format("%02d", month) + " reset successfully.");
    }

    public double CALCULATE_SALARY(int month, int year) {
        int presentDays = 0;
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) {
            LocalDate d = LocalDate.parse(record.GETDATE());
            if (d.getMonthValue() == month && d.getYear() == year && record.ISPRESENT()) presentDays++;
        }
        return presentDays * SALARYPERDAY;
    }

    public int GET_DAYS_PRESENT(int month, int year) {
        int count = 0;
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) {
            LocalDate d = LocalDate.parse(record.GETDATE());
            if (d.getMonthValue() == month && d.getYear() == year && record.ISPRESENT()) count++;
        }
        return count;
    }

    public int GET_DAYS_ABSENT(int month, int year) {
        int count = 0;
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) {
            LocalDate d = LocalDate.parse(record.GETDATE());
            if (d.getMonthValue() == month && d.getYear() == year && !record.ISPRESENT()) count++;
        }
        return count;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(EMPLOYEEID).append(",").append(NAME).append(",").append(SALARYPERDAY);
        for (ATTENDANCERECORD record : ATTENDANCERECORDS) sb.append(";").append(record.toString());
        return sb.toString();
    }

    public static EMPLOYEE FROMSTRING(String line) {
        line = line.trim();
        if (line.isEmpty()) throw new IllegalArgumentException("Empty employee line");
        String[] parts = line.split(";", 2);
        String[] main = parts[0].split(",");
        if (main.length < 3) throw new IllegalArgumentException("Invalid employee header: " + parts[0]);
        int id = Integer.parseInt(main[0].trim());
        String name = main[1].trim();
        double salary = Double.parseDouble(main[2].trim());
        EMPLOYEE emp = new EMPLOYEE(id, name, salary);
        if (parts.length > 1 && !parts[1].trim().isEmpty()) {
            String[] records = parts[1].split(";");
            for (String r : records) {
                r = r.trim();
                if (!r.isEmpty()) emp.GETATTENDANCERECORDS().add(ATTENDANCERECORD.FROMSTRING(r));
            }
        }
        return emp;
    }
}

class HR {
    public Map<Integer, EMPLOYEE> EMPLOYEEMAP;
    private List<EMPLOYEE> EMPLOYEES;
    private final String FILE_NAME = "employees.txt";
    private int NEXT_EMPLOYEEID = 1;

    public HR() {
        EMPLOYEES = new ArrayList<>();
        EMPLOYEEMAP = new HashMap<>();
        LOAD_FROM_FILE();
        UPDATE_NEXT_EMPLOYEEID();
    }

    private void UPDATE_NEXT_EMPLOYEEID() {
        for (EMPLOYEE emp : EMPLOYEES) {
            if (emp.GETEMPLOYEEID() >= NEXT_EMPLOYEEID) NEXT_EMPLOYEEID = emp.GETEMPLOYEEID() + 1;
        }
    }

    public int GENERATE_EMPLOYEEID() { return NEXT_EMPLOYEEID++; }

    public void ADD_EMPLOYEE(String name, double salaryPerDay) {
        int id = GENERATE_EMPLOYEEID();
        EMPLOYEE emp = new EMPLOYEE(id, name, salaryPerDay);
        EMPLOYEES.add(emp);
        EMPLOYEEMAP.put(id, emp);
        System.out.println("Employee added successfully with ID: " + id);
    }

    public void REMOVE_EMPLOYEE(int employeeID) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) {
            EMPLOYEES.remove(emp);
            EMPLOYEEMAP.remove(employeeID);
            System.out.println("Employee removed successfully.");
        } else System.out.println("Employee not found!");
    }

    public void SHOW_EMPLOYEES() {
        System.out.println("List of Employees:");
        for (EMPLOYEE emp : EMPLOYEES)
            System.out.println("ID: " + emp.GETEMPLOYEEID() + ", Name: " + emp.GETNAME() +
                    ", Salary/Day: " + emp.GETSALARYPERDAY());
    }

    public void MARK_ATTENDANCE(int employeeID, String date, boolean isPresent) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) emp.MARK_ATTENDANCE(date, isPresent);
        else System.out.println("Employee not found!");
    }

    public void UPDATE_ATTENDANCE(int employeeID, String date, boolean isPresent) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) emp.UPDATE_ATTENDANCE(date, isPresent);
        else System.out.println("Employee not found!");
    }

    public void RESET_ALL_ATTENDANCE(int employeeID) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) emp.RESET_ALL_ATTENDANCE();
        else System.out.println("Employee not found!");
    }

    public void RESET_ATTENDANCE_BY_MONTH(int employeeID, int month, int year) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) emp.RESET_ATTENDANCE_BY_MONTH(month, year);
        else System.out.println("Employee not found!");
    }

    public void CALCULATE_MONTHLY_SALARY(int employeeID, int month, int year) {
        EMPLOYEE emp = EMPLOYEEMAP.get(employeeID);
        if (emp != null) {
            double salary = emp.CALCULATE_SALARY(month, year);
            System.out.println(emp.GETNAME() + "'s salary for " + year + "-" +
                    String.format("%02d", month) + ": " + salary);
        } else System.out.println("Employee not found!");
    }

    public void GENERATE_MONTHLY_ATTENDANCE_REPORT(int month, int year) {
        System.out.println("Attendance Report for " + year + "-" + String.format("%02d", month));
        for (EMPLOYEE emp : EMPLOYEES) {
            int present = emp.GET_DAYS_PRESENT(month, year);
            int absent = emp.GET_DAYS_ABSENT(month, year);
            System.out.println("ID: " + emp.GETEMPLOYEEID() + ", Name: " + emp.GETNAME() +
                    ", Present: " + present + ", Absent: " + absent);
        }
    }

    public void SAVE_TO_FILE() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(FILE_NAME))) {
            for (EMPLOYEE emp : EMPLOYEES) pw.println(emp.toString());
        } catch (IOException e) {
            System.out.println("Error saving data: " + e.getMessage());
        }
    }

    public void LOAD_FROM_FILE() {
        File file = new File(FILE_NAME);
        if (!file.exists()) return;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            int lineNo = 0;
            while ((line = br.readLine()) != null) {
                lineNo++;
                line = line.trim();
                if (line.isEmpty()) continue;
                try {
                    EMPLOYEE emp = EMPLOYEE.FROMSTRING(line);
                    EMPLOYEES.add(emp);
                    EMPLOYEEMAP.put(emp.GETEMPLOYEEID(), emp);
                } catch (Exception ex) {
                    System.out.println("Warning: could not parse line " + lineNo + ": " + ex.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("Error loading data: " + e.getMessage());
        }
    }
}

public class AttendanceTracker {
    private static Scanner SC = new Scanner(System.in);
    private static HR HR_SYSTEM = new HR();
    private static int CURRENT_YEAR = LocalDate.now().getYear();

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- EMPLOYEE ATTENDANCE TRACKER ---");
            System.out.println("1. EMPLOYEES");
            System.out.println("2. ATTENDANCE");
            System.out.println("3. CALCULATE MONTHLY SALARY");
            System.out.println("4. GENERATE MONTHLY ATTENDANCE REPORT");
            System.out.println("5. EXIT");
            System.out.print("CHOOSE AN OPTION: ");
            int choice = READ_INT();
            switch (choice) {
                case 1 -> EMPLOYEES_MENU();
                case 2 -> ATTENDANCE_MENU();
                case 3 -> CALCULATE_SALARY_MENU();
                case 4 -> GENERATE_REPORT_MENU();
                case 5 -> {
                    HR_SYSTEM.SAVE_TO_FILE();
                    System.out.println("Data saved. Exiting...");
                    SC.close();
                    System.exit(0);
                }
                default -> System.out.println("INVALID OPTION. TRY AGAIN.");
            }
        }
    }

    private static void EMPLOYEES_MENU() {
        while (true) {
            System.out.println("\n--- EMPLOYEES MENU ---");
            System.out.println("1. LIST EMPLOYEES");
            System.out.println("2. ADD EMPLOYEE");
            System.out.println("3. REMOVE EMPLOYEE");
            System.out.println("4. BACK");
            System.out.print("CHOOSE AN OPTION: ");
            int choice = READ_INT();
            switch (choice) {
                case 1 -> HR_SYSTEM.SHOW_EMPLOYEES();
                case 2 -> {
                    System.out.print("ENTER NAME: ");
                    String name = SC.nextLine();
                    System.out.print("ENTER SALARY PER DAY: ");
                    double salary = READ_DOUBLE();
                    HR_SYSTEM.ADD_EMPLOYEE(name, salary);
                }
                case 3 -> {
                    System.out.print("ENTER EMPLOYEE ID TO REMOVE: ");
                    int id = READ_INT();
                    HR_SYSTEM.REMOVE_EMPLOYEE(id);
                }
                case 4 -> { return; }
                default -> System.out.println("INVALID OPTION. TRY AGAIN.");
            }
        }
    }

    private static void ATTENDANCE_MENU() {
        while (true) {
            System.out.println("\n--- ATTENDANCE MENU ---");
            System.out.println("1. MARK ATTENDANCE");
            System.out.println("2. UPDATE ATTENDANCE");
            System.out.println("3. RESET ATTENDANCE");
            System.out.println("4. BACK");
            System.out.print("CHOOSE AN OPTION: ");
            int choice = READ_INT();
            switch (choice) {
                case 1 -> MARK_ATTENDANCE();
                case 2 -> UPDATE_ATTENDANCE();
                case 3 -> RESET_ATTENDANCE();
                case 4 -> { return; }
                default -> System.out.println("INVALID OPTION. TRY AGAIN.");
            }
        }
    }

    private static void MARK_ATTENDANCE() {
        System.out.print("ENTER EMPLOYEE ID: ");
        int empId = READ_INT();
        String date = READ_MONTH_DAY();
        boolean status = READ_PRESENT_ABSENT();
        HR_SYSTEM.MARK_ATTENDANCE(empId, date, status);
    }

    private static void UPDATE_ATTENDANCE() {
        System.out.print("ENTER EMPLOYEE ID: ");
        int empId = READ_INT();
        EMPLOYEE emp = HR_SYSTEM.EMPLOYEEMAP.get(empId);
        if (emp == null) { System.out.println("EMPLOYEE NOT FOUND!"); return; }

        List<ATTENDANCERECORD> records = emp.GETATTENDANCERECORDS();
        if (records.isEmpty()) { System.out.println("NO ATTENDANCE RECORDS FOUND."); return; }

        System.out.println("ATTENDANCE RECORDS:");
        for (int i = 0; i < records.size(); i++) {
            ATTENDANCERECORD r = records.get(i);
            System.out.println((i + 1) + ". " + r.GETDATE() + " - " + (r.ISPRESENT() ? "Present" : "Absent"));
        }

        System.out.print("SELECT RECORD NUMBER TO UPDATE: ");
        int idx = READ_INT();
        if (idx < 1 || idx > records.size()) { System.out.println("INVALID SELECTION."); return; }

        ATTENDANCERECORD r = records.get(idx - 1);
        boolean newStatus = READ_PRESENT_ABSENT();
        r.SETPRESENT(newStatus);
        System.out.println("Attendance updated successfully for " + r.GETDATE());
    }

    private static void RESET_ATTENDANCE() {
        System.out.print("ENTER EMPLOYEE ID: ");
        int empId = READ_INT();
        System.out.println("1. RESET ALL ATTENDANCE RECORDS");
        System.out.println("2. RESET ATTENDANCE FOR SPECIFIC MONTH");
        System.out.println("3. BACK");
        System.out.print("CHOOSE AN OPTION: ");
        int choice = READ_INT();
        if (choice == 1) HR_SYSTEM.RESET_ALL_ATTENDANCE(empId);
        else if (choice == 2) {
            int month = READ_MONTH();
            HR_SYSTEM.RESET_ATTENDANCE_BY_MONTH(empId, month, CURRENT_YEAR);
        }
    }

    private static void CALCULATE_SALARY_MENU() {
        System.out.print("ENTER EMPLOYEE ID: ");
        int empId = READ_INT();
        int month = READ_MONTH();
        HR_SYSTEM.CALCULATE_MONTHLY_SALARY(empId, month, CURRENT_YEAR);
    }

    private static void GENERATE_REPORT_MENU() {
        int month = READ_MONTH();
        HR_SYSTEM.GENERATE_MONTHLY_ATTENDANCE_REPORT(month, CURRENT_YEAR);
    }

    private static int READ_INT() {
        while (true) {
            try { return Integer.parseInt(SC.nextLine().trim()); }
            catch (NumberFormatException e) { System.out.print("INVALID INPUT. ENTER A NUMBER: "); }
        }
    }

    private static double READ_DOUBLE() {
        while (true) {
            try { return Double.parseDouble(SC.nextLine().trim()); }
            catch (NumberFormatException e) { System.out.print("INVALID INPUT. ENTER A NUMBER: "); }
        }
    }

    private static int READ_MONTH() {
        while (true) {
            System.out.print("ENTER MONTH (1-12): ");
            int month = READ_INT();
            if (month >= 1 && month <= 12) return month;
            System.out.println("INVALID MONTH. TRY AGAIN.");
        }
    }

    private static String READ_MONTH_DAY() {
        while (true) {
            System.out.print("ENTER DATE (MM-DD): ");
            String input = SC.nextLine().trim();
            try {
                String[] parts = input.split("-");
                if (parts.length != 2) throw new Exception();
                int month = Integer.parseInt(parts[0]);
                int day = Integer.parseInt(parts[1]);
                LocalDate d = LocalDate.of(CURRENT_YEAR, month, day);
                return d.toString();
            } catch (Exception e) { System.out.println("INVALID DATE FORMAT. USE MM-DD."); }
        }
    }

    private static boolean READ_PRESENT_ABSENT() {
        while (true) {
            System.out.print("ENTER STATUS (Present/Absent): ");
            String input = SC.nextLine().trim().toLowerCase();
            if (input.equals("present")) return true;
            if (input.equals("absent")) return false;
            System.out.println("INVALID INPUT. TYPE 'Present' OR 'Absent'.");
        }
    }
}
