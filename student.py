from person import Person
class Student(Person):
    def __init__(self, name, age, salary, year):
        #inheritance super()
        super().__init__(name,age,salary)
        self.academic_year= year
    def say_hi(self):
        return f'Hello {self.name} as student'
    