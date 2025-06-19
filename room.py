class Room:
    room_type = ["ICU", "General", "Private", "Emergency"]

    def __init__(self, room_number, room_type, capacity, current_occupancy:bool, equipment_list:list, daily_rate, number_of_equipments:int):
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = capacity
        self.current_occupancy = current_occupancy
        self.equipment_list = equipment_list
        self.daily_rate = daily_rate
        self.number_of_equipments = number_of_equipments
    
    def __str__(self):
        return f"""
        Room Infos: /nRoom Number: {self.room_number} 
        Room Type: {self.room_type}
        Capacity: {self.capacity}
        Current Occupancy: {self.is_available()}
        Equipment List: {self.equipment_list}
        Daily Rate: {self.daily_rate}
        """
    
    def is_available(self):
        if self.current_occupancy:
            return "Room is Available"
        else:
            return "Room isn't available"
    
    def manage_equipments(self, equipment):
        while True:
            decision = input("0 to remove equipment, 1 to add equipment")
            if decision == 1:
                #For he context, we can also check if we really wanna add another same quipment even if it's already existing in the list
                self.equipment_list.append(equipment)
                return "Equipment added successfully"
            elif decision == 0:
                self.equipment_list.remove(equipment)
                return "Equipment removed successfully"
