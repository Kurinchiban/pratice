from enum import Enum
import random
import time
import string

# creating the enum class for the vehicle type
class VehicleType(Enum):
    BIKE = 1 
    CAR = 2
    VAN = 3

# creating the class for the checkpoint type
class CheckpointType(Enum):
    ENTRYPOINT = 1
    EXITPOINT = 2

# creating the class for the payment type
class PaymentType(Enum):
    CARD = 1
    CASH = 2
    UPI = 3

# creating the class for the parking_lot
class ParkingLot:
    # Attributes - name,address
    def __init__(self,name,address):
        self.name = name 
        self.address = address 
        self.floors = [] 
        self.checkpoints = [] 

    def display_floor_count(self):
        """ This function will display the floor count in the parking lot """
        print(len(self.floors))

    def display_checkpoint_count(self):
        """ This function will display the checkpoint count in the parking lot """
        print(len(self.checkpoints))

    def adding_floor(self,floor):
        """ This function will do the operation to add a floor to the parking lot """
        self.floors.append(floor)

    def removing_floor(self,floor):
        """ This function will do the operation to remove a floor from the parking lot """
        self.floors.remove(floor)

    def adding_checkpoint(self,checkpoint):
        """ This function will do the operation to add a entry and exit checkpoint to the parking lot """
        self.checkpoints.append(checkpoint)

    def removing_checkpoint(self,checkpoint):
        """ This function will do the operation to remove a entry and exit checkpoint to the parking lot """
        self.checkpoints.remove(checkpoint)
   
    def display_board(self):
        """ This function will display the number of remaining spots in each floor"""
        # Iterating the floors
        for floor in self.floors:
            car = 0
            bike = 0 
            van = 0
            print("-------{}-------".format(floor.name))
            # iterating the spots
            for spot in floor.spots:
                # cheking the free spot for car
                if (spot.vehicle_type == VehicleType.CAR) and (spot.is_free == True ):
                    car += 1 
                # cheking the free spot for bike
                elif (spot.vehicle_type == VehicleType.BIKE) and (spot.is_free == True ):
                    bike += 1
                # cheking the free spot for van
                elif (spot.vehicle_type == VehicleType.VAN) and (spot.is_free == True ):
                    van += 1
            print("Spot available in the {} : " .format(floor.name))
            print("     CAR  : {} ".format(car))
            print("     BIKE  : {} ".format(bike))
            print("     VAN  : {} ".format(van))

    def __str__(self):
        return 'Name of Parking_Lot : {} , adress of parking_Lot : {} '.format(self.name,self.address)

# creating the class for the parking floor  
class ParkingFloor:
    # Attributes : name
    def __init__(self,name):
        self.name=name
        self.spots = []

    def display_spots_id(self):
        """ This function will return the spotid for the each spot """
        for spot in self.spots:
            print(spot.spot_id)

    def display_spots_count(self):
        """ This function will return the count of the spots located in the floor"""
        return len(self.spots)
    
    def check_spot_available(self,vehicle):
        """ This function will will do the operation to check the spot available for the given type of the vehicle """
        for spot in self.spots:
            if (spot.vehicle_type == vehicle.vehicle_type) and (spot.is_free == True):
                return True

    def assigning_spot_id (self,vehicle):
        """ This function will do the operation to assign the spot_id for the given type of vehicle which make the spot occupied and return the spot_id"""
        for spot in self.spots:
            # checking the spot for the required vehicle type and finding is_free
            if (spot.vehicle_type == vehicle.vehicle_type) and (spot.is_free == True):
                spot.is_free = False 
                return spot.spot_id
    
    def unassigning_spot_id (self,spot_id):
        """ This function will do the operation to unassign the spot_id for the vehicle and make the spot un occupied"""
        for spot in self.spots:
            # checking the requird spot id in that floor
            if (spot.spot_id == spot_id):
                spot.is_free = True

    def adding_spot(self,spot):
        """ This function will do the operation to add the spot to the spots  """
        self.spots.append(spot)

    def removing_spot(self,spot):
        """ This function will do the operation to remove the spot to the spots"""
        self.spots.remove(spot)

# creating the class for the Parking_spot
class ParkingSpot:
    # Attributes : spot_id, vehicle_type, is free
    def __init__(self,spot_id,vehicle_type,is_free):
        self.spot_id = spot_id 
        self.vehicle_type = vehicle_type  
        self.is_free = is_free

class Checkpoint:
    # Attributes : name, floor, type_of_checkpoint
    def __init__(self,name,floor,type_of_checkpoint):
        self.name = name 
        self.floor = floor 
        self.type_of_checkpoint=type_of_checkpoint 

# creating the class for the Ticket
class Ticket:
    # Attributes : ticket_id,checkpoint,spot_id,floor,vehicle_number,in_time,payment_status,amount_to_pay
    def __init__(self,ticket_id,checkpoint,spot_id,floor,vehicle_number,in_time,payment_status):
        self.ticket_id = ticket_id
        self.checkpoint = checkpoint
        self.spot_id = spot_id  
        self.floor = floor
        self.vehicle_number = vehicle_number
        self.in_time = in_time
        self.out_time = None
        self.payment_status = payment_status
        self.amount_to_pay = None

    def update_payment_status(self):
        """ This function will will do the operation to change the payment_status of the ticket"""
        self.payment_status = True

    def get_outtime(self,time):
        """This function will outime and add it to the vehicle"""
        self.out_time = time

    def __str__(self):
        return "Ticket_id : {},checkpoint : {} ,spot_id : {} ,floor : {} ,vehicle_number : {} ,in_time : {},payment_status : {} ".format(self.ticket_id,self.checkpoint.name,self.spot_id,self.floor.name,self.vehicle_number,self.in_time,self.payment_status)

# creating the class for the system
class System :
    
    def is_spot_available(self,floor,vehicle):
        """ This function will check the spot available for the given type of the vehicle """
        if floor.check_spot_available(vehicle):
            return True
        else:
            return False    

    def assign_spot_id(self,floor,vehicle):
        """ This function will assign the spot_id for the given type of vehicle which make the spot occupied and return the spot_id"""
        return floor.assigning_spot_id (vehicle)
        
    def in_time(self):
        """ This function is will return the curren time"""
        return time.time()

    def generate_ticket_id(self):
        """ This function will generate the ticket_id and return it"""
        id = random.choice(string.digits) + random.choice(string.ascii_lowercase)
        return id

    def process_entry(self,customer,floor,checkpoint):
        """ This function will generate a ticket for the customer and add it to the customet """
        # checking the floor spots to find the spot available for the given vehicle 
        if system.is_spot_available(floor,customer.vehicle):
            """ This function will assign the spot_id for the given type of vehicle which make the spot occupied and return the spot_id"""
            spot_id=system.assign_spot_id(floor,customer.vehicle)
            time=system.in_time()
            ticket_id=system.generate_ticket_id()
            # creating the ticket for the customer
            ticket=Ticket(ticket_id,checkpoint,spot_id,floor,customer.vehicle.vehicle_number,time,False)
            # giving the ticket for the customer
            customer.get_ticket(ticket)
            print("Entry completed for : {} which came from : {} ".format(customer.vehicle.vehicle_number,checkpoint.name))
        else:
            print("Sorry no spot available for your vehicle in this {} ".format(floor.name))

    def process_exit(self,customer,check_point):
        # checking the customer had paid for the ticket
        if customer.ticket.payment_status :
            print("Exit completed for : {} you can exit through : {} ".format(customer.ticket.vehicle_number,check_point.name))
            # This function will unassign the spot_id for the vehicle and make the spot un occupied
            system.un_assign_spot(customer.ticket.floor,customer.ticket.spot_id)
            pass 
        else:
            print("You have to process the payment")

    def generate_spot_id(self,random_number):
        """ This function will generate the spot_id and return it"""
        id = str(random_number) + random.choice(string.ascii_lowercase)
        return id

    def un_assign_spot(self,floor,spot_id):
        """This function will unassign the spot_id for the vehicle and make the spot un occupied"""
        return floor.unassigning_spot_id (spot_id)
         
    def out_time(self):
        """ This function is will return the curren time"""
        return time.time() 

    def calculate_duration(self,in_time,out_time):
        """ This function is will return the duration spent by the vehicle inside the lot"""
        duration=out_time-in_time
        return duration

    def calculate_amount (self,duration):
        """ This function is will return the amount based on the duration spent by the vehicle inside the lot"""
        if (int(duration) < 3600) :
            return 40 
        elif (int(duration) < 7200) :
            return 30 
        elif int(duration) < 10800:
            return 25 

    def scan_ticket(self,ticket):
        current_time = system.out_time()
        # calculate duration
        ticket.get_outtime(current_time)
        duration_spent_in_parkinglot = system.calculate_duration(ticket.in_time,current_time)
        # calculat amount
        amount_to_pay = system.calculate_amount(duration_spent_in_parkinglot)
        # will add the amount to pay in the ticket attribute
        ticket.amount_to_pay = amount_to_pay
        print("You have to pay : {} ".format(amount_to_pay))


# creating the class for the system
class Admin ():

    def add_floor(self,floor):
        """ This function will add a floor to the parking lot """
        P.adding_floor(floor)

    def remove_floor(self,floor):
        """ This function will remove a floor from the parking lot """
        P.removing_floor(floor)

    def add_checkpoint(self,checkpoint):
        """ This function will add a entry and exit point to the parking lot """
        P.adding_checkpoint(checkpoint)
    
    def remove_checkpoint(self,checkpoint):
        """ This function will remove a entry and exit point from the parking lot """
        P.removing_checkpoint(checkpoint)

    def add_spot(self,floor,type_of_vehicle,No_of_space):
        """ This function will add the spot to the spots  """
        # checking the type of the vehicle
        if type_of_vehicle == VehicleType.CAR or type_of_vehicle == VehicleType.VAN or type_of_vehicle == VehicleType.BIKE:
            # iterating the number of spots to add
            for space in range(No_of_space):
                spot_id = system.generate_spot_id(space)
                vehicle_type = type_of_vehicle
                spot=ParkingSpot(spot_id,vehicle_type,True)
                # adding spots to the floor
                floor.adding_spot(spot)

    def remove_spot(self,floor,type_of_vehicle,No_of_space):
        """ This function will remove the spot to the spots  """
        # checking the type of vehicle
        if type_of_vehicle == VehicleType.CAR or type_of_vehicle == VehicleType.VAN or type_of_vehicle == VehicleType.BIKE :
            # iterating the number of space to remove
            for _ in No_of_space:
                # iterating the spots
                for spot in floor.spots:
                    # checking vehicle type
                    if (spot.vehicle_type == type_of_vehicle) and (spot.is_free == True):
                        # removing the spot to the floor
                        floor.removing_spot(spot) 
    
# creating the class for the Parking_spot
class Vehicle:
    # Attributes : vehicle_number, vehicle_type
    def __init__(self,vehicle_number,vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

# creating the class for the Customer
class Customer:
    # Attributes : name, vehicle, type
    def __init__(self,customer_name,vehicle):
        self.customer_name = customer_name
        self.vehicle = vehicle
        self.ticket = None

    def get_ticket(self,ticket):
        """ This function will add the ticket to the ticket attributes"""
        self.ticket = ticket

# creating the class for the Payment
class Payment:

    def process_payment(self,ticket,amount,mode_of_payment):
        """ This function will pay the amount for the ticket and change the payment_status of the ticket"""
        # check the mode of payment and the amount
        if ((mode_of_payment == PaymentType.CARD) and (ticket.amount_to_pay == amount)) or ((mode_of_payment == PaymentType.CASH) and (ticket.amount_to_pay == amount)) or ((mode_of_payment == PaymentType.UPI) and (ticket.amount_to_pay == amount)):
            # changing the payment status of the ticket
            ticket.update_payment_status()
            print( "You have paid the amount Thanks for coming" )

if __name__ == '__main__':

    # creating the parking lot
    P = ParkingLot("BTC","PTC,Chennai")  
    # Display the name and address of the parking_lot
    print(P)     
    print()
    
    # creating the admin,system and payment for the parking_lot
    admin=Admin()
    system=System()
    payment=Payment()

    # adding the floor to the parkinglot 
    floor_1 = ParkingFloor("floor_1")
    # adding the entrance checkpoint for the floor_1
    e1f1=Checkpoint("E1F1",floor_1,CheckpointType.ENTRYPOINT)
    # adding the exit checkpoint for the floor_1
    ex1f1=Checkpoint("EX1F1",floor_1,CheckpointType.EXITPOINT)
    
    admin.add_floor(floor_1)
    admin.add_checkpoint(e1f1)
    admin.add_checkpoint(ex1f1)

    # adding spots for Floor_1 
    admin.add_spot(floor_1,VehicleType.CAR,3)
    admin.add_spot(floor_1,VehicleType.VAN,3)
    admin.add_spot(floor_1,VehicleType.BIKE,3)

    # Will display the number of spot available in the parking lot
    P.display_board()
    print()

    # customer 1 entrance
    C1 = Customer("Kumar",Vehicle('TN A5454',VehicleType.CAR))
    system.process_entry(C1,floor_1,e1f1)

    # customer 2 entrance
    C2 = Customer("Lokesh",Vehicle('TN B9000',VehicleType.BIKE))
    system.process_entry(C2,floor_1,e1f1)

    # customer 3 entrance
    C3 = Customer("RAJ",Vehicle('TN C9001',VehicleType.VAN))
    system.process_entry(C3,floor_1,e1f1)
    print()

    time.sleep(2)

    # customer 3 scan ticket
    system.scan_ticket(C3.ticket)
    # customer 3 process payment
    payment.process_payment(C3.ticket,40,PaymentType.CARD)
    # customer 3 exit
    system.process_exit(C3,ex1f1)
    print()
    
    P.display_board()