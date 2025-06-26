from abc import abstractmethod
class Person:
    
    def __init__(self,  person_id, name, age, gender, phone, email, address, emergency_contact:dict):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone 
        self.email = email
        self.address = address 
        self.emergency_contact = emergency_contact
    
    @abstractmethod
    def get_role(self):
        pass
