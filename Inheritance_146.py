#Python Inheritance Practical Programs

#1.Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)
m = Manager(101, "Tanvi", 50000, "IT")
m.display_manager()


#2.Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print("Discounted Price:", final_price)
c = Car("Toyota", "Innova", "Diesel", 2500000)
c.display_car()
c.discounted_price(10)

#3.Create two classes Academic and Sports. Academic stores marks obtained by a student, while Sports stores sports points. Create Student that inherits from both classes and calculates overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def performance(self):
        print("Name:", self.name)
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.marks + self.sports_points)
s = Student("Tanvi", 85, 15)
s.performance()



#4.Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create Employee that inherits from both classes and displays complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
e = Employee("Tanvi", 20, 101, "Developer", 50000)
e.display()



#5.Create a class Person containing name and age. Derive Student from Person with roll number and course. Further derive ResearchStudent from Student with research topic and guide name. Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)
r = ResearchStudent("Tanvi", 20, 101, "Computer Engineering",
                    "Artificial Intelligence", "Dr. Sharma")
r.display()


#6.Create a base class BankAccount with account number and balance. Derive SavingsAccount with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)
p = PremiumSavingsAccount("ACC101", 100000, 7, "Free Insurance")
p.display()

#7.Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.

class Shape:
    def display(self, name):
        print("Shape:", name)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
c = Circle(7)
c.display("Circle")
print("Area:", c.area())
r = Rectangle(10, 5)
r.display("Rectangle")
print("Area:", r.area())
t = Triangle(10, 8)
t.display("Triangle")
print("Area:", t.area())



#8.Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
class Manager(Employee):
    def salary(self):
        return self.basic_salary + (self.basic_salary * 0.30)
class Developer(Employee):
    def salary(self):
        return self.basic_salary + (self.basic_salary * 0.20)
class Tester(Employee):
    def salary(self):
        return self.basic_salary + (self.basic_salary * 0.15)
m = Manager(101, "Amit", 50000)
d = Developer(102, "Rahul", 40000)
t = Tester(103, "Priya", 35000)
print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())



#9.Create a class Person. Derive Student and Faculty from Person. Create TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no
class Faculty(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id
class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, faculty_id):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.faculty_id = faculty_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student Roll No:", self.roll_no)
        print("Faculty ID:", self.faculty_id)
ta = TeachingAssistant("Tanvi", 20, 101, "F201")
ta.display()


#10.Create a base class Vehicle. Derive Car and Bike from Vehicle. Create SportsCar inheriting from Car and ElectricBike inheriting from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class SportsCar(Car):
    def speed(self):
        print("Sports car has high speed.")
class ElectricBike(Bike):
    def battery(self):
        print("Electric bike has rechargeable battery.")
sc = SportsCar("BMW", "M4")
sc.display()
print("Model:", sc.model)
sc.speed()
eb = ElectricBike("Ola", "S1")
eb.display()
print("Model:", eb.model)
eb.battery()


#11.Create a base class Student with attributes roll_no, name, and course. Derive Result that stores marks in three subjects and calculates total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course
class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.marks = [m1, m2, m3]

    def calculate(self):
        total = sum(self.marks)
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)
r = Result(101, "Tanvi", "Computer Engineering", 85, 90, 88)
r.calculate()



#12.Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self, discount):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(discount))
p = ElectronicProduct(101, "Laptop", 60000, "Dell", "2 Years")
p.display(10)



#13.Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing document...")
class Scanner:
    def scan_document(self):
        print("Scanning document...")
class MultifunctionDevice(Printer, Scanner):
    def multifunction(self):
        self.print_document()
        self.scan_document()
device = MultifunctionDevice()
device.multifunction()



#14.Create classes Camera and Phone. Camera provides methods for taking photographs, while Phone provides methods for making calls. Create Smartphone inheriting from both.

class Camera:
    def take_photo(self):
        print("Photograph taken.")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and phone operations.")
s = Smartphone()
s.display()
s.take_photo()
s.make_call("9876543210")

#15.Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)
r = ResearchStudent("Tanvi", 20, 101, "Computer Engineering",
                    "Machine Learning", "Dr. Patil")
r.display()



#16.Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)
r = ResearchStudent("Tanvi", 20, 102, "Computer Engineering",
                    "Artificial Intelligence", "Dr. Sharma")
r.display()



#17.Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")
class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")
d = Dog("Bruno")
d.display()
d.sound()
c = Cat("Kitty")
c.display()
c.sound()
w = Cow("Gauri")
w.display()
w.sound()


#18.Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization
class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease
class Surgeon(Doctor):
    def surgery(self):
        print("Surgeon performs surgery.")
class MedicalResearcher(Doctor, Patient):
    def research(self):
        print("Medical researcher performs medical research.")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)
s = Surgeon("Dr. Amit", 40, "Cardiology")
print("Surgeon:", s.name)
print("Specialization:", s.specialization)
s.surgery()
mr = MedicalResearcher("Dr. Priya", 35, "Research", "Diabetes")
mr.display()
mr.research()

