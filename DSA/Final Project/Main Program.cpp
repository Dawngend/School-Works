#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <cstring>

using namespace std;


class Room {
private:
    int roomNumber;
    string roomType;
    string status;
    time_t checkInTime;
    time_t checkOutTime;
public:
    Room(int num, string type) : roomNumber(num), roomType(type), status("Available") {}
   
    int getRoomNumber() const { return roomNumber; }
    string getRoomType() const { return roomType; }
    string getStatus() const { return status; }
    time_t getCheckInTime() const { return checkInTime; }
    time_t getCheckOutTime() const { return checkOutTime; }
   
    void setStatus(string s) { status = s; }
    void checkIn() {
        status = "Occupied";
        checkInTime = time(NULL);
    }
    void checkOut() {
        status = "Currently cleaning";
        checkOutTime = time(NULL);
    }
    void cleanComplete() { status = "Available"; }
   
    void display() const {
        cout << "Room " << roomNumber << " (" << roomType << ") - " << status;
        if (status == "Occupied") {
            struct tm* timeinfo = localtime(&checkInTime);
            char buffer[80];
            strftime(buffer, sizeof(buffer), "%a %b %d %H:%M:%S", timeinfo);
            cout << " since " << buffer << endl;
        } else if (status == "Currently cleaning") {
            struct tm* timeinfo = localtime(&checkOutTime);
            char buffer[80];
            strftime(buffer, sizeof(buffer), "%a %b %d %H:%M:%S", timeinfo);
            cout << " since " << buffer << endl;
        } else {
            cout << endl;
        }
    }
};


class Customer {
private:
    string lastName;
    string firstName;
    string phoneNumber;
    int guests;
    int duration;
    bool loyaltyMember;
    time_t birthDate;
    int roomAssigned;
public:
    Customer(string last, string first, string phone, int g, int d)
        : lastName(last), firstName(first), phoneNumber(phone), guests(g), duration(d),
          loyaltyMember(false), roomAssigned(-1) {}
   
    string getName() const { return lastName + ", " + firstName; }
    string getPhone() const { return phoneNumber; }
    int getGuests() const { return guests; }
    int getDuration() const { return duration; }
    bool isLoyaltyMember() const { return loyaltyMember; }
    int getRoom() const { return roomAssigned; }
    time_t getBirthDate() const { return birthDate; }
   
    void setLoyaltyMember(bool l) { loyaltyMember = l; }
    void setBirthDate(time_t bd) { birthDate = bd; }
    void assignRoom(int room) { roomAssigned = room; }
    void setDuration(int d) { duration = d; }
   
    void display() const {
        cout << "Customer: " << getName() << endl;
        cout << "Phone: " << phoneNumber << endl;
        cout << "Guests: " << guests << endl;
        cout << "Duration: " << duration << " hours" << endl;
        if (roomAssigned != -1) {
            cout << "Room: " << roomAssigned << endl;
        }
        if (loyaltyMember) {
            cout << "Loyalty Member (30% discount applied)" << endl;
        }
    }
};


struct LoyaltyNode {
    Customer* customer;
    LoyaltyNode* next;
   
    LoyaltyNode(Customer* c) : customer(c), next(NULL) {}
};


struct ReservationNode {
    Customer* customer;
    Room* room;
    string idPass; 
    ReservationNode* next;
   
    ReservationNode(Customer* c, Room* r, string id) 
        : customer(c), room(r), idPass(id), next(NULL) {}
};


class ParkInnSystem {
private:
    vector<Room*> rooms;
    ReservationNode* reservations;
    LoyaltyNode* loyaltyMembers;
    int dailyReservations;
   
    void loadLoyaltyMembers() {
        ifstream file("LoyaltyProgram.txt");
        if (file.is_open()) {
            string line;
            while (getline(file, line)) {
                size_t pos1 = line.find('|');
                size_t pos2 = line.find('|', pos1+1);
               
                string namePart = line.substr(0, pos1);
                string phone = line.substr(pos1+1, pos2-pos1-1);
                string bdayStr = line.substr(pos2+1);
               
                size_t commaPos = namePart.find(',');
                string last = namePart.substr(0, commaPos);
                string first = namePart.substr(commaPos+1);
               
                Customer* member = new Customer(last, first, phone, 0, 0);
                member->setLoyaltyMember(true);
               
                struct tm tm;
                memset(&tm, 0, sizeof(struct tm));
                sscanf(bdayStr.c_str(), "%d-%d-%d", &tm.tm_year, &tm.tm_mon, &tm.tm_mday);
                tm.tm_year -= 1900;
                tm.tm_mon--;
                member->setBirthDate(mktime(&tm));
               
                LoyaltyNode* newNode = new LoyaltyNode(member);
                newNode->next = loyaltyMembers;
                loyaltyMembers = newNode;
            }
            file.close();
        }
    }
   
    void saveLoyaltyMembers() {
        ofstream file("LoyaltyProgram.txt");
        if (file.is_open()) {
            LoyaltyNode* current = loyaltyMembers;
            while (current != NULL) {
                time_t bday = current->customer->getBirthDate();
                struct tm* tm = localtime(&bday);
                char bdayStr[11];
                strftime(bdayStr, sizeof(bdayStr), "%Y-%m-%d", tm);
                file << current->customer->getName() << "|"
                     << current->customer->getPhone() << "|"
                     << bdayStr << endl;
                current = current->next;
            }
            file.close();
        }
    }
   
    Customer* findLoyaltyMember(const string& phone) {
        LoyaltyNode* current = loyaltyMembers;
        while (current != NULL) {
            if (current->customer->getPhone() == phone) {
                return current->customer;
            }
            current = current->next;
        }
        return NULL;
    }
   
    void loadDailyReservations() {
        ifstream file("Reservations.txt");
        if (file.is_open()) {
            file >> dailyReservations;
            file.close();
        } else {
            dailyReservations = 0;
        }
    }
   
    void saveDailyReservations() {
        ofstream file("Reservations.txt");
        if (file.is_open()) {
            file << dailyReservations;
            file.close();
        }
    }
    
    
   
    float calculatePrice(string roomType, int duration) {
        if (roomType == "Econo") {
            if (duration <= 3) return 480.0;
            if (duration <= 6) return 960.0;
            return 1700.0;
        } else if (roomType == "Premium") {
            if (duration <= 3) return 640.0;
            if (duration <= 6) return 1100.0;
            return 2000.0;
        } else {
            if (duration <= 3) return 1300.0;
            if (duration <= 6) return 1900.0;
            return 2500.0;
        }
    }
   
    string generateIdPass() {
        static const char alphanum[] =
            "0123456789"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "abcdefghijklmnopqrstuvwxyz";
        string pass;
       
        for (int i = 0; i < 8; ++i) {
            pass += alphanum[rand() % (sizeof(alphanum) - 1)];
        }
       
        return pass;
    }
   
public:
    ParkInnSystem() : reservations(NULL), loyaltyMembers(NULL), dailyReservations(0) {
        for (int i = 101; i <= 110; i++) rooms.push_back(new Room(i, "Econo"));
        for (int i = 201; i <= 210; i++) rooms.push_back(new Room(i, "Premium"));
        for (int i = 301; i <= 310; i++) rooms.push_back(new Room(i, "Deluxe"));
       
        loadLoyaltyMembers();
        loadDailyReservations();
        srand(time(NULL));
    }
   
    ~ParkInnSystem() {
        for (size_t i = 0; i < rooms.size(); i++) {
            delete rooms[i];
        }
       
        ReservationNode* resCurrent = reservations;
        while (resCurrent != NULL) {
            ReservationNode* next = resCurrent->next;
            if (!resCurrent->customer->isLoyaltyMember()) {
                delete resCurrent->customer;
            }
            delete resCurrent;
            resCurrent = next;
        }
       
        LoyaltyNode* loyCurrent = loyaltyMembers;
        while (loyCurrent != NULL) {
            LoyaltyNode* next = loyCurrent->next;
            delete loyCurrent->customer;
            delete loyCurrent;
            loyCurrent = next;
        }
       
        saveLoyaltyMembers();
        saveDailyReservations();
    }
   
    void displayMainMenu() {
        cout << "\n=== D'yan lang Apartelle ===" << endl;
        cout << "1. Quick Reservation" << endl;
        cout << "2. Room System" << endl;
        cout << "3. Check Out" << endl;
        cout << "4. View All Rooms" << endl;
        cout << "5. View Loyalty Program Members" << endl;
        cout << "6. View Current Reservations" << endl;
        cout << "7. Exit" << endl;
        cout << "Daily Reservations: " << dailyReservations << endl;
        cout << "Enter choice: ";
    }
   
    void quickReservation() {
        string lastName, firstName, phone;
        int guests, duration;
       
        cout << "\n=== Quick Reservation ===" << endl;
        cout << "Last Name: ";
        cin >> lastName;
        cout << "First Name: ";
        cin >> firstName;
        cin.ignore(1000, '\n');
        
        cout << "Phone Number: ";
        getline(cin, phone);
        cout << "Number of Guests: ";
        while (!(cin >> guests) || guests < 1) {
            cout << "Invalid input! Please enter a positive number: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }
        cout << "Duration (hours): ";
        while (!(cin >> duration) || duration < 1) {
            cout << "Invalid input! Please enter a positive number: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }
       
        Customer* customer = findLoyaltyMember(phone);
        if (customer != NULL) {
            cout << "Welcome back, " << customer->getName() << "! Loyalty discount applied." << endl;
            customer->setDuration(duration);
        } else {
            customer = new Customer(lastName, firstName, phone, guests, duration);
        }
       
        cout << "\nAvailable Rooms:" << endl;
        vector<Room*> availableRooms;
        for (size_t i = 0; i < rooms.size(); i++) {
            if (rooms[i]->getStatus() == "Available") {
                availableRooms.push_back(rooms[i]);
                rooms[i]->display();
            }
        }
       
        if (availableRooms.empty()) {
            cout << "No available rooms!" << endl;
            if (!customer->isLoyaltyMember()) {
                delete customer;
            }
            return;
        }
       
        cout << "Enter room number to assign: ";
        int roomNum;
        while (!(cin >> roomNum)) {
            cout << "Invalid input! Please enter a room number: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }
       
        Room* selectedRoom = NULL;
        for (size_t i = 0; i < availableRooms.size(); i++) {
            if (availableRooms[i]->getRoomNumber() == roomNum) {
                selectedRoom = availableRooms[i];
                break;
            }
        }
       
        if (selectedRoom == NULL) {
            cout << "Invalid room selection!" << endl;
            if (!customer->isLoyaltyMember()) {
                delete customer;
            }
            return;
        }
       
        customer->assignRoom(roomNum);
        selectedRoom->checkIn();
       
        string idPass = generateIdPass();
        ReservationNode* newNode = new ReservationNode(customer, selectedRoom, idPass);
        newNode->next = reservations;
        reservations = newNode;
       
        dailyReservations++;
       
        cout << "\nReservation Complete!" << endl;
        cout << "=== Official Receipt ===" << endl;
        customer->display();
        selectedRoom->display();
       
        float basePrice = calculatePrice(selectedRoom->getRoomType(), duration);
        float finalPrice = customer->isLoyaltyMember() ? basePrice * 0.7 : basePrice;
       
        cout << "Base Price: P" << fixed << setprecision(2) << basePrice << endl;
        if (customer->isLoyaltyMember()) {
            cout << "Discount (30%): P" << fixed << setprecision(2) << (basePrice * 0.3) << endl;
        }
        cout << "Total Price: P" << fixed << setprecision(2) << finalPrice << endl;
        cout << "ID Pass: " << idPass << endl;
    }
   
    void roomSystem() {
        cout << "\n=== Room System ===" << endl;
        cout << "\nEnter room number: ";
        int roomNum;
        while (!(cin >> roomNum)) {
            cout << "Invalid input! Please enter a room number: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }
       
        Room* room = NULL;
        for (size_t i = 0; i < rooms.size(); i++) {
            if (rooms[i]->getRoomNumber() == roomNum) {
                room = rooms[i];
                break;
            }
        }
       
        if (room == NULL || room->getStatus() != "Occupied") {
            cout << "Room not occupied or invalid!" << endl;
            return;
        }
       
        int choice;
        do {
            cout << "\nRoom " << roomNum << " System" << endl;
            cout << "1. Check remaining time" << endl;
            cout << "2. Order food and drinks" << endl;
            cout << "3. Extend time" << endl;
            cout << "4. Call for home service" << endl;
            cout << "5. Return to main menu" << endl;
            cout << "Enter choice: ";
            
            while (!(cin >> choice)) {
                cout << "Invalid input! Please enter a number (1-5): ";
                cin.clear();
                cin.ignore(10000, '\n');
            }
            
            switch (choice) {
                case 1: {
                    time_t now = time(NULL);
                    time_t checkIn = room->getCheckInTime();
                    double elapsed = difftime(now, checkIn) / 3600.0;
                   
                    int duration = 0;
                    ReservationNode* current = reservations;
                    while (current != NULL) {
                        if (current->room->getRoomNumber() == roomNum) {
                            duration = current->customer->getDuration();
                            break;
                        }
                        current = current->next;
                    }
                   
                    double remaining = duration - elapsed;
                    cout << "Remaining time: " << fixed << setprecision(1) << remaining << " hours" << endl;
                    break;
                }
                case 2:
                    cout << "Food and drinks menu coming soon!" << endl;
                    break;
                case 3: {
                    ReservationNode* current = reservations;
                    while (current != NULL) {
                        if (current->room->getRoomNumber() == roomNum) {
                            break;
                        }
                        current = current->next;
                    }
                   
                    if (current == NULL) {
                        cout << "Reservation not found!" << endl;
                        break;
                    }
                   
                    cout << "Current duration: " << current->customer->getDuration() << " hours" << endl;
                    cout << "Enter additional hours: ";
                    int extra;
                    while (!(cin >> extra) || extra < 1) {
                        cout << "Invalid input! Please enter a positive number: ";
                        cin.clear();
                        cin.ignore(10000, '\n');
                    }
                   
                    float extensionPrice;
                    if (current->room->getRoomType() == "Econo") {
                        extensionPrice = 160.0;
                    } else if (current->room->getRoomType() == "Premium") {
                        extensionPrice = 200.0;
                    } else {
                        extensionPrice = 400.0;
                    }
                   
                    float finalPrice = current->customer->isLoyaltyMember() ? extensionPrice * 0.8 : extensionPrice;
                   
                    cout << "Extension Price: P" << fixed << setprecision(2) << finalPrice;
                    if (current->customer->isLoyaltyMember()) {
                        cout << " (20% discount applied)";
                    }
                    cout << endl;
                   
                    cout << "Confirm extension? (y/n): ";
                    char confirm;
                    cin >> confirm;
                   
                    if (confirm == 'y' || confirm == 'Y') {
                        current->customer->setDuration(current->customer->getDuration() + extra);
                        cout << "Time extended successfully!" << endl;
                    }
                    break;
                }
                case 4:
                    cout << "Home service requested. Staff will contact you shortly." << endl;
                    break;
                case 5:
                    cout << "Returning to main menu..." << endl;
                    break;
                default:
                    cout << "Invalid choice! Please try again." << endl;
            }
        } while (choice != 5);
    }
   
    void checkOut() {
        cout << "\n=== Check Out ===" << endl;
        cout << "\nEnter room number: ";
        int roomNum;
        cin >> roomNum;

        ReservationNode* prev = NULL;
        ReservationNode* current = reservations;
        while (current != NULL) {
            if (current->room->getRoomNumber() == roomNum) {
                break;
            }
            prev = current;
            current = current->next;
        }

        if (current == NULL || current->room->getStatus() != "Occupied") {
            cout << "Invalid room or room not occupied!" << endl;
            return;
        }

        cout << "Enter ID Pass for verification: ";
        string inputIdPass;
        cin >> inputIdPass;

        if (inputIdPass != current->idPass) {
            cout << "Invalid ID Pass! Check-out denied." << endl;
            return;
        }

        cout << "\nChecking out:" << endl;
        current->customer->display();
        current->room->display();
        current->room->checkOut();

        if (!current->customer->isLoyaltyMember()) {
            cout << "\nWould you like to join our loyalty program? (y/n): ";
            char join;
            cin >> join;
           
            if (join == 'y' || join == 'Y') {
                cout << "Enter birthdate (YYYY-MM-DD): ";
                string bdayStr;
                cin >> bdayStr;
               
                struct tm tm;
                memset(&tm, 0, sizeof(struct tm));
                sscanf(bdayStr.c_str(), "%d-%d-%d", &tm.tm_year, &tm.tm_mon, &tm.tm_mday);
                tm.tm_year -= 1900;
                tm.tm_mon--;
                time_t bday = mktime(&tm);
               
                current->customer->setLoyaltyMember(true);
                current->customer->setBirthDate(bday);
               
                LoyaltyNode* newNode = new LoyaltyNode(current->customer);
                newNode->next = loyaltyMembers;
                loyaltyMembers = newNode;
               
                cout << "Thank you for joining! You'll get 30% discount on future stays and 20% on extensions." << endl;
                cout << "Free complimentary meal on your next visit!" << endl;
            }
        }

        cout << "\nPlease return the ID Pass." << endl;
        cout << "Thank you for staying at D'yan lang Apartelle!" << endl;
        cout << "Come again soon!" << endl;

        if (prev == NULL) {
            reservations = current->next;
        } else {
            prev->next = current->next;
        }

        if (!current->customer->isLoyaltyMember()) {
            delete current->customer;
        }
        delete current;
    }
   
    void viewAllRooms() {
        cout << "\n=== All Rooms ===" << endl;
        for (size_t i = 0; i < rooms.size(); i++) {
            rooms[i]->display();
        }
    }
   
    void viewLoyaltyMembers() {
        cout << "\n=== Loyalty Program Members ===" << endl;
        if (loyaltyMembers == NULL) {
            cout << "No loyalty members yet." << endl;
            return;
        }
        
        LoyaltyNode* current = loyaltyMembers;
        int count = 1;
        while (current != NULL) {
            cout << count++ << ". " << current->customer->getName() << endl;
            cout << "   Phone: " << current->customer->getPhone() << endl;
            
            time_t bday = current->customer->getBirthDate();
            struct tm* tm = localtime(&bday);
            char bdayStr[11];
            strftime(bdayStr, sizeof(bdayStr), "%Y-%m-%d", tm);
            cout << "   Birthdate: " << bdayStr << endl;
            
            current = current->next;
        }
    }
    
    void viewCurrentReservations() {
        cout << "\n=== Current Reservations ===" << endl;
        if (reservations == NULL) {
            cout << "No current reservations." << endl;
            return;
        }
        
        ReservationNode* current = reservations;
        int count = 1;
        while (current != NULL) {
            cout << count++ << ". " << current->customer->getName() << endl;
            cout << "   Room: " << current->room->getRoomNumber() << " (" 
                 << current->room->getRoomType() << ")" << endl;
            cout << "   Duration: " << current->customer->getDuration() << " hours" << endl;
            cout << "   ID Pass: " << current->idPass << endl;
            if (current->customer->isLoyaltyMember()) {
                cout << "   Loyalty Member (30% discount)" << endl;
            }
            cout << endl;
            
            current = current->next;
        }
    }
   
    void run() {
        int choice;
        do {
            displayMainMenu();
            
            while (!(cin >> choice)) {
                cout << "Invalid input! Please enter a number (1-7): ";
                cin.clear();
                cin.ignore(10000, '\n');
            }
            
            switch (choice) {
                case 1:
                    quickReservation();
                    break;
                case 2:
                    roomSystem();
                    break;
                case 3:
                    checkOut();
                    break;
                case 4:
                    viewAllRooms();
                    break;
                case 5:
                    viewLoyaltyMembers();
                    break;
                case 6:
                    viewCurrentReservations();
                    break;
                case 7:
                    cout << "Exiting system..." << endl;
                    break;
                default:
                    cout << "Invalid choice! Please enter a number between 1 and 7." << endl;
            }
        } while (choice != 7);
    }
};

int main() {
    ParkInnSystem system;
    system.run();
    return 0;
}
