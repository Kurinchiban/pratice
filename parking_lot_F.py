
from enum import Enum
import random
import time

#creating the enum for the vehicleType
class VehicleType(Enum):
    BIKE = 1 
    CAR = 2
    VAN = 3

class SpotType(Enum):
    FREE = 1 
    TAKEN = 2 

class Payment_Type(Enum):
    CASH=1 
    CARD=2 
    GPAY=3 
    
class Parkinglot:
    # Attributes - name,address
    def __init__(self,name,address):
        self.name = name 
        self.address = address 
        self.floors = [] 
        self. entrance = [] 
        self .exit = [] 
    
    # This function will add the floors to the parking lot
    def add_floors(self,floor):
        self.floors.append(floor)

    # This function will add the entrance to the parking lot
    def add_entrance(self,entrance):
        self.entrance.append(entrance)

    # This function will add the entrance to the parking lot
    def add_exit(self,exit):
        self.exit.append(exit)

    def assign_entrance(self):
        entrance=random.choice(self.entrance)
        return entrance

    def assign_exit(self):
        exit=random.choice(self.exit)
        return exit
    
    def display_floor(self):
        print(self.floors)

    def display_entrance(self):
        print(self.entrance) 

    def display_exit(self):
        print(self.exit)

class Entrance (Parkinglot):
    def __init__ (self): 
        self.entrance = P.assign_entrance()
 
    def process_Entry(self,ticket):
        # Iterating the floors              
        for floor in P.floors:
            # checking the specific vehicle type is free are not
            if floor.spots[ticket.vehicle.type][SpotType.FREE]:
                # assigning the spot to the ticket using the assign_spot function
                ticket.spot=floor.assign_spot(ticket)
                print('Entry Completed For : ', ticket.vehicle.vehicle_number)
                break 

class Exit(Parkinglot):
    def __init__(self):
        self.entrance = P.assign_entrance()

    def calculate_amount(): 
        pass
    
    def process_amount():
        pass

    def process_exit(self,ticket):
        # iterating the floor 
        for floor in P.floors :
            # checking the ticket spot available inside the floor
            if ticket.spot in floor.spots[ticket.vehicle.type][SpotType.TAKEN] :
                # unassigning the spot to the ticket using the unassign_spot function
                floor.unassignSpot(ticket)
                break
        ticket.spots    = None 
        print('Exit Completed For  : ', ticket.vehicle.vehicle_number)
        print(ticket)
        
    def display_e(self):
        print(self.entrance) 
 
class Parking_floor:
    def __init__(self):
        self.spots= { VehicleType.BIKE : { SpotType.FREE:[] , SpotType.TAKEN :[] },
                      VehicleType.CAR : {  SpotType.FREE:[] , SpotType.TAKEN :[] },
                      VehicleType.VAN : { SpotType.FREE:[] , SpotType.TAKEN :[] } }
    
    # assign a spot for the ticket
    def assign_spot(self,ticket):
        if self.spots[ticket.vehicle.type][SpotType.FREE] != [] :
            spot = self.spots[ticket.vehicle.type][SpotType.FREE].pop()
            ticket.spot = spot
            self.spots[ticket.vehicle.type][SpotType.TAKEN].append(spot)
            return ticket.spot
        return False
    
    # unassign a spot for the ticket
    def unassignSpot(self, ticket) :
        self.spots[ticket.vehicle.type][SpotType.FREE].append(ticket.spot)
        self.spots[ticket.vehicle.type][SpotType.TAKEN].remove(ticket.spot)

    def add_spot(self,type,number): 
        for i in range (number):
            spot=Spot(type)
            self.spots[type][SpotType.FREE].append(spot)
 
    def remove_spot(self,type,number):
        for i in range (number):
            spot=Spot(type)
            self.spots[type][SpotType.FREE].remove(spot)

class Spot:
    def __init__(self,type):
         self.type = type 

class Ticket:
    def __init__ (self,customer_name,vehicle):
        self.customer_name = customer_name
        self.vehicle=vehicle
        self.intime=time.time()
        self.outime=None 
        self.floor=None  
        self.spot=None 

    def payment_status():
        pass  

# creating the class for the vehicle 
class Vehicle:
    # Attributes - Vehicle_number 
    def __init__(self,vehicle_number):
        self.vehicle_number=vehicle_number

# creating the class for the Bike which is inheritance of the vehicle 
class Bike(Vehicle):
    def __init__ (self,vehicle_number):
        super().__init__(vehicle_number)
        self.type= VehicleType.BIKE

# creating the class for the Car which is inheritance of the vehicle 
class Car(Vehicle):
    def __init__ (self,vehicle_number):
        super().__init__(vehicle_number)
        self.type= VehicleType.CAR

# creating the class for the Van which is inheritance of the vehicle 
class Van(Vehicle):
    def __init__ (self,vehicle_number):
        super().__init__(vehicle_number)
        self.type= VehicleType.VAN

class DisplayBoard:
    def show(self, P) :
        for floor in P.floors:
            print(P.name)
            print('Car  : ', len(floor.spots[VehicleType.CAR][SpotType.FREE]))
            print('Bike : ', len(floor.spots[VehicleType.BIKE][SpotType.FREE]))
            print('Van : ', len(floor.spots[VehicleType.VAN][SpotType.FREE]))

class Payment:
    def __init__():
        def __init__ (self,amount):
            self.amount = amount

class Cash(Payment):
    def __init__ (self,amount):
        super().__init__(amount)
        self.type= Payment_Type.CASH

class Cash(Payment):
    def __init__ (self,amount):
        super().__init__(amount)
        self.type= Payment_Type.CASH 

class Cash(Payment):
    def __init__ (self,amount):
        super().__init__(amount)
        self.type= Payment_Type.CASH 


if __name__ == '__main__':
    # creating the parking lot
    P=Parkinglot('Google Parking Lot', '123, Fort, Mumbai')
    
    # Adding the entrance for the parking floor
    # Adding the entrance for the parking floor
    P.add_entrance("Entrance_ 1")
    P.add_exit("Exit_1")
    
    F1 = Parking_floor()
    P.add_floors(F1)

    F1.add_spot(VehicleType.CAR, 3)
    F1.add_spot(VehicleType.BIKE, 3)
    F1.add_spot(VehicleType.VAN, 3)
    
    E1 = Entrance()
    P.add_entrance(E1)

    Ex1 = Exit()
    P.add_exit(Ex1)

    Board = DisplayBoard()
    Board.show(P)

    T1 = Ticket("Kumar",Car('TN A5454'))
    E1.process_Entry(T1)

    T2 = Ticket("Lokesh",Bike('TN B9000'))
    E1.process_Entry(T2)

    T3 = Ticket("raj",Van('TN C9001'))
    E1.process_Entry(T3)
    
    print(" ----------------- ")
    time.sleep(2)  
    Ex1.process_exit(T2)
 
    print(" ------------------ ")
    Board = DisplayBoard() 
    Board.show(P)
 