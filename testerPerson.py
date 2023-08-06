from person import Person
from student import Student
from teacher import Teacher
def main():
    Nidhal = Person("Nidhal ALAmri", 24,1500)
    #it wil cosider ali 20 years old by default
    p2= Person("ali",23,1500)
    std1= Student("latifa", 12,2022,333)
    std2= Student("hala",18,2012,400)
    print(std1.descrip())
    print(std2.say_hi())
    #another way
    print(Student.say_hi(std1))

    print(p2.descrip())
    print(Nidhal.get_name())
    Nidhal.set_name("Nidhal")
    print(Nidhal.get_name())
    print(Nidhal.descrip())
    Nidhal.run()
    
    t1= Teacher("lama",44,"DB",1500)
    #overriding method ( same method but for diffrent classes/obj)
    print(t1.say_hi())
    
    #getting the method from parent 
    print(std2.say_hii())
    
main()