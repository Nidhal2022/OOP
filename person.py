class Person:
    #constructor to creat obj
    #initialize instance var
    #default constructor age=20
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary= salary
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,newName):
        self.name = newName
    def set_age(self,newAge):
        self.age = newAge
        
    def run(self):
        print(self.name, "is running")
    
    def descrip(self):
        return f'Person name {self.name} is {self.age} years old'
    
    def say_hii(self):
        return f'hi {self.name} as Person'
    
    def bounse(self):
        b= self.salary*0.005
        return b
        
        
