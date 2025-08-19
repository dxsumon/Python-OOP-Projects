class Bus:
    def __init__(self,  number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    def available_seats(self):
        return self.total_seats - self.booked_seats
    def booking_seats(self):
        available_total_seats = self.available_seats()
        if available_total_seats > 0:
            self.booked_seats += 1
            return True
        print(f"We have only {self.total_seats - self.booked_seats} seats!")
        return False
    
class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
class Bus_System_class:
    def __init__(self):
        self.bus_list = []
        self.passenger_list = []
class Admin:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    def log_in(self, user_name, password):
        if user_name == self.user_name and password == self.password:
            return True
        else:
            return False
         
bus1 = Bus(200, "Dhaka to Gazipur", 40)
