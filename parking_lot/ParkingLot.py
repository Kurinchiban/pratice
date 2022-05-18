from enum import Enum
import random
import time

class VehicleType(Enum):
    BIKE = 1 
    CAR = 2
    VAN = 3

# creating the class for the parking_lot
class Parking_Lot:
    # Attributes - name,address
    def __init__(self,name,address):
        self.name = name 
        self.address = address 
        self.floors = [] 
        self.entrance = [] 
        self.exit = [] 
        self.ticket = [] 

# creating the class for the parking floor  
class Parking_Floor:
    def __init__(self):
        self.spots = []

    def generate_spot_id():
        pass

# creating the class for the Parking_spot
class Parking_Spot:
    def __init__(self):
        self.spot_id = None 
        self.vehicle_type = None   
        self.is_free = None 

# creating the class for the Ticket
class Ticket:

    ticket_id=0 

    def __init__(self):
        self.ticket_id = None 
        self.spot_id = None   
        self.floor = None
        self.vehicle_number = None 
        self.in_time = None 
        self.payment_status = None 

    def generate_ticket_id():
        pass

# creating the class for the entrance
class Entrance:
    def process_Entry(self,vehicle):
        # Iterating the floors              
        for floor in P.floors:
            if floor.is_spot_available(vehicle):
                spot_id=floor.assign_spot(floor,vehicle)
                time=floor.intime(vehicle)
                ticket_id=floor.generate_ticket(vehicle)
                ticket=Ticket(ticket_id,spot_id,floor,vehicle.vehicle_number,time,False)
                P.ticket.append(ticket)
            else:
                continue 
        else:
            print("Sorry for the inconvenience All the spots in the Parking lot is occupied ")

# creating the class for the entrance
class Exit:
    def process_Exit(self,vehicle):
        for ticket in P.ticket:
            if ticket.vehicle_number == vehicle.number :
                if ticket.payment_status :
                    ticket.un_assign(ticket.floor,ticket.spot_id)
                    P.ticket.remove(ticket)
                else:
                    print("You have not paid the amount for parking your vehicle please process the payment")
                    ticket.process_payment(vehicle,ticket)
                    vehicle.process_Exit(vehicle)

# creating the class for the system
class System (Parking_Lot,Parking_Floor):
    def __init__():
        super().__init__()

    def is_spot_available(self,vehicle):
        for spot in self.spots:
            if (spot.vehile_type == vehicle.vehicle_type) and (spot.is_free == True):
                return True 
        else:
            return False    

    def assign_spot(floor,vehicle):
        for spot in floor.spots:
            if (spot.vehicle_type == vehicle.vehicle_type) and (spot.is_free == True):
                spot.is_free = False 
                return spot.id

    def un_assign_spot(floor,spot_id):
        for spot in floor.spots:
            if (spot.spot_id == spot_id):
                spot.is_free = True 
                return spot.id

# creating the class for the system
class Admin (Parking_Lot,Parking_Floor):
    def __init__():
        super().__init__()

    def add_spot(Floor,Type_of_vehicle,No_of_Vehicle):
        if Type_of_vehicle == VehicleType.CAR or Type_of_vehicle == VehicleType.VAN or Type_of_vehicle == VehicleType.BIKE:
            for vehicle_count in No_of_Vehicle:
                spot_id = Floor.generate_spot_id()
                vehicle_type = Type_of_vehicle
                spot=Parking_Spot(spot_id,vehicle_type,True)
                Floor.spots.append(spot)

    def remove_spot(Floor,Type_of_vehicle,No_of_Vehicle):
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

if __name__ == '__main__':

    # creating the parking lot
    P=Parking_Lot("BTC","PTC,Chennai")       