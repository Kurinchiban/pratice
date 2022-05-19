from enum import Enum
import random
import time
import string

class VehicleType(Enum):
    BIKE = 1 
    CAR = 2
    VAN = 3

# creating the class for the parking_lot
class ParkingLot:
    # Attributes - name,address
    def __init__(self,name,address):
        self.name = name 
        self.address = address 
        self.floors = [] 
        self.entrance = [] 
        self.exit = [] 
        self.ticket = [] 

    def display_floor_count(self):
        print(len(self.floors))

    def display_entrance_count(self):
        print(len(self.entrance))

    def display_exit_count(self):
        print(len(self.exit))

    def display_ticket_count(self):
        print(len(self.ticket))

    def __str__(self):
        return 'Name of Parking_Lot : {} , adress of parking_Lot : {} '.format(self.name,self.address)   

# creating the class for the parking floor  
class ParkingFloor:
    def __init__(self):
        self.spots = []

    def generate_spot_id(self,random_number):
        id = str(random_number) + random.choice(string.ascii_lowercase)
        return id

    def display_spots_id(self):
        for spot in self.spots:
            print(spot.spot_id)

    def display_spots_count(self):
        return len(self.spots)

# creating the class for the Parking_spot
class Parking_Spot:
    def __init__(self,spot_id,vehicle_type,is_free):
        self.spot_id = spot_id 
        self.vehicle_type = vehicle_type  
        self.is_free = is_free

# creating the class for the Ticket
class Ticket:

    def __init__(self,ticket_id,spot_id,floor,vehicle_number,in_time,payment_status):
        self.ticket_id = ticket_id
        self.spot_id = spot_id  
        self.floor = floor
        self.vehicle_number = vehicle_number
        self.in_time = in_time
        self.payment_status = payment_status

# creating the class for the entrance
class Entrance:

    def process_Entry(self,vehicle):
        # Iterating the floors              
        for floor in P.floors:
            if system.is_spot_available(floor,vehicle):
                spot_id=system.assign_spot(floor,vehicle)
                time=system.in_time()
                ticket_id=system.generate_ticket_id()
                ticket=Ticket(ticket_id,spot_id,floor,vehicle.vehicle_number,time,False)
                P.ticket.append(ticket)
            else:
                continue 
        
# creating the class for the entrance
class Exit:

    def process_Exit(self,vehicle):
        for ticket in P.ticket:
            if ticket.vehicle_number == vehicle.vehicle_number :
                if ticket.payment_status :
                    system.un_assign_spot(ticket.floor,ticket.spot_id)
                    P.ticket.remove(ticket)
                    break
                else:
                    print("You have not paid the amount for parking your vehicle please process the payment")
                    payment.process_payment(ticket)
                    Ex1.process_Exit(vehicle)
                    break

# creating the class for the system
class System :
    
    ticket_id=1

    def assign_entrance(self):
        entrance=random.choice(P.entrance)
        return entrance
    
    def assign_exit(self):
        exit=random.choice(P.exit)
        return exit
     
    def is_spot_available(self,floor,vehicle):
        for spot in floor.spots:
            if (spot.vehicle_type == vehicle.vehicle_type) and (spot.is_free == True):
                return True 
        else:
            return False    

    def assign_spot(self,floor,vehicle):
        for spot in floor.spots:
            if (spot.vehicle_type == vehicle.vehicle_type) and (spot.is_free == True):
                spot.is_free = False 
                return spot.spot_id
    
    def in_time(self):
        return time.time()

    def generate_ticket_id(self):
        id = str(System.ticket_id) + random.choice(string.ascii_lowercase)
        System.ticket_id += 1 
        return id

    def un_assign_spot(self,floor,spot_id):
        for spot in floor.spots:
            if (spot.spot_id == spot_id):
                spot.is_free = True 

    def out_time(self):
        return time.time() 

    def calculate_duration(self,in_time,out_time):
        duration=out_time-in_time
        return duration

    def calculate_amount (self,duration):
        if (int(duration) < 3600) :
            return 50 
        elif (int(duration) < 7200) :
            return 100 
        elif int(duration) < 10800:
            return 150 
        elif int(duration) < 14400:
            return 200 

# creating the class for the system
class Admin ():

    def add_floor(self,floor):
        P.floors.append(floor)

    def remove_floor(self,floor):
        P.floors.remove(floor)

    def add_entrance(self,entrance):
        P.entrance.append(entrance)

    def remove_entrance(self,entrance):
        P.entrance.remove(entrance)

    def add_exit(self,exit):
        P.exit.append(exit)

    def remove_exit(self,exit):
        P.exit.remove(exit) 

    def add_spot(self,Floor,Type_of_vehicle,No_of_space):
        if Type_of_vehicle == VehicleType.CAR or Type_of_vehicle == VehicleType.VAN or Type_of_vehicle == VehicleType.BIKE:
            for space in range(No_of_space):
                spot_id = Floor.generate_spot_id(space)
                vehicle_type = Type_of_vehicle
                spot=Parking_Spot(spot_id,vehicle_type,True)
                Floor.spots.append(spot)

    def remove_spot(self,Floor,Type_of_vehicle,No_of_Vehicle):
        if Type_of_vehicle == VehicleType.CAR or Type_of_vehicle == VehicleType.VAN or Type_of_vehicle == VehicleType.BIKE :
            for vehicle_count in No_of_Vehicle:
                for spot in Floor.spots:
                    if (spot.vehicle_type == Type_of_vehicle) and (spot.is_free == True):
                        Floor.spots.remove(spot) 
    
# creating the class for the Parking_spot
class Vehicle:
    def __init__(self,vehicle_number,vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

# creating the class for the Customer

class Customer:
    def __init__(self,customer_name,vehicle):
        self.customer_name=customer_name
        self.vehicle=vehicle

# creating the class for the Payment
class Payment:
    def process_payment(self,ticket):
        current_out_time = system.out_time()
        current_duration = system.calculate_duration(ticket.in_time,current_out_time)
        current_amount = system.calculate_amount(current_duration)
        mode_of_payment = input("Enter your mode of transport card/cash/upi-scan : ")
        amount_to_paid = int(input("You have to pay {} : ".format(current_amount)))
        if ((mode_of_payment == "card") and (amount_to_paid == current_amount)) or ((mode_of_payment == "cash") and (amount_to_paid == current_amount)) or ((mode_of_payment == "upi-scan") and (amount_to_paid == current_amount)):
            ticket.payment_status = True
            print( "You have paid the amount Thanks for coming" )


if __name__ == '__main__':

    # creating the parking lot
    P = ParkingLot("BTC","PTC,Chennai")  
    print(P)     
    
    # creating the admin,system and payment for the parking_lot
    admin=Admin()
    system=System()
    payment=Payment()

    # adding the floor_1 to the parkinglot 
    floor_1 = ParkingFloor()
    admin.add_floor(floor_1)

    E1 = Entrance()
    admin.add_entrance(E1)

    Ex1 = Exit()
    admin.add_exit(Ex1)

    # P.display_floor_count()
    # P.display_entrance_count()
    # P.display_exit_count()

    # adding spots for Floor_1 

    admin.add_spot(floor_1,VehicleType.CAR,3)
    admin.add_spot(floor_1,VehicleType.VAN,3)
    admin.add_spot(floor_1,VehicleType.BIKE,3)

    C1 = Customer("Kumar",Vehicle('TN A5454',VehicleType.CAR))
    E1.process_Entry(C1.vehicle)

    C2 = Customer("Lokesh",Vehicle('TN B9000',VehicleType.BIKE))
    E1.process_Entry(C2.vehicle)

    C3 = Customer("RAJ",Vehicle('TN C9001',VehicleType.VAN))
    E1.process_Entry(C3.vehicle)

    P.display_ticket_count()

    time.sleep(2)

    Ex1.process_Exit(C3.vehicle)
    
    P.display_ticket_count()

 

