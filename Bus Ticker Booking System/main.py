import time

class Bus:
    def __init__(self,  number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = int(total_seats)
        self.booked_seats = 0
        
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        print("No seats available!")
        return False
    
class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus    
        
class Bus_System_class:
    bus_list = []
    passenger_list = []
    
    def book_ticket(self, bus_number, name, phone_number):
        for bus in self.bus_list:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone_number, bus)
                    self.passenger_list.append(passenger)
                    print(f"Ticket booked successfully for {name}")
                    print(f"Bus: {bus.number} | Route: {bus.route}")
                    print(f"Seat Confirmed, Remaining seats: {bus.available_seats()}")
                    return
                else:
                    print("Sorry, no seats available on this bus.")
                    return
        print("This Bus is not available!")

class Admin(Bus_System_class):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def log_in(self, user_name, password):
        if user_name == self.user_name and password == self.password:
            print("Login Successful!")
            return True
        else:
            return False
        
    def add_buses(self, number, route, seats):
        new_bus = Bus(number, route, seats)
        for bus in self.bus_list:
            if bus.number == new_bus.number:
                print("This Bus already exists")
                return
        self.bus_list.append(new_bus)
        print("Bus added successfully")
    
    def display_all_buses(self):
        if len(self.bus_list) == 0:
            print("No Bus available right now! Please wait.")
        for bus in self.bus_list:
            print(f"Bus number: {bus.number} | Route: {bus.route} | "
                  f"Total seats: {bus.total_seats} | Available seats: {bus.available_seats()}")


def admin_menu(admin_obj):
    while True:
        print("\n.....Welcome to admin panel.....\n1.Add buses\n2.View all buses\n3.Logout")
        admin_input = input("Enter your choice: ")
        if admin_input.isdigit():
            admin_choice = int(admin_input)
            if admin_choice == 1:
                number = input("Enter bus number: ")
                route = input("Enter bus route: ")
                seats = int(input("Enter total bus seats: "))
                admin_obj.add_buses(number,route,seats)
            elif admin_choice == 2:
                admin_obj.display_all_buses()
            elif admin_choice == 3:
                return
            else:
                print("Type only 1-3")
        else:
            print("Input can be only number!!!")
        
def user_menu(admin):
    while True:
        print("\n.....Welcome to online bus ticket.....")
        print("1.Admin login\n2.Book ticket\n3.View Buses\n4.Exit")
        user_input = input("Enter your choice: ")
        if user_input.isdigit():
            user_choice = int(user_input)
            if user_choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                print("Loading", end="", flush=True)
                for i in range(10):
                    time.sleep(0.20)
                    print(".", end="", flush=True)
                print("")
                if admin.log_in(username, password):
                    admin_menu(admin)
                else:
                    print("Username and password wrong! Please Try Again...")
                    
            elif user_choice == 2:
                bus_number = input("Enter bus number: ")
                name = input("Enter passenger name: ")
                phone = input("Enter passenger phone: ")
                admin.book_ticket(bus_number, name, phone)

            elif user_choice == 3:
                admin.display_all_buses()
            elif user_choice == 4:
                break
            else:
                print("Type only 1-4")
        else:
            print("Input can be only number!!!")


admin = Admin("admin", "1234")
user_menu(admin)
