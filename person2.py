from person import Person
from teacher import Teacher
def main():
    p1=Person('ali',24,1500)
    t1=Teacher('noor',22,'db',1500)
    print(p1.descrip())
    print(p1.bounse())
    print(t1.descrip())
    print(t1.bounse())
       
main()