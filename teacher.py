from person import Person

class Teacher(Person):
    def __init__(self,name,age,course,salary):
        super().__init__(name,age,salary)
        self.tcourse= course
        
        
    def say_hi(self):
        #CALLING PERSON METHOD THEN THE TEACHER
        print(super().say_hii())
        return f'iam {self.name} a {self.tcourse} teacher prepare yourself!'
    def bounse(self):
        tb=super().bounse() * 2
        return tb
        
    