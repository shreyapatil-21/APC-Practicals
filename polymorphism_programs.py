#1.Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes and override the area() method in each class. Create objec
#class Shapets of each class and demonstrate runtime polymorphism.
class Shape:
    def area(self):
        print("area of shape")
class Circle(Shape):
    def area(self):
        r=5
        print("area of circle is:",3.14*r*r)
class Rectangle(Shape):
    def area(self):
        l=4
        b=2
        print("area of rectangle is:",l*b)
class Triangle(Shape):
    def area(self):
        b=6
        h=7
        print("area of triangle is:",0.5*b*h)
c=Circle()
r=Rectangle()
t=Triangle()
c.area()
r.area()
t.area()
        
#2.	Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and Tester classes. Override the method in each class to calculate salary according to the employee's role.
class Employee:
    def cal_salary(self, sal):
        self.sal = sal


class Manager(Employee):
    def cal_salary(self, sal):
        self.sal = sal
        print("Salary of Manager is:", self.sal + self.sal * 25 / 100)


class Developer(Employee):
    def cal_salary(self, sal):
        self.sal = sal
        print("Salary of Developer is:", self.sal + self.sal * 20 / 100)


class Tester(Employee):
    def cal_salary(self, sal):
        self.sal = sal
        print("Salary of Tester is:", self.sal + self.sal * 15 / 100)


m = Manager()
d = Developer()
t = Tester()

m.cal_salary(500000)
d.cal_salary(500000)
t.cal_salary(500000)

#3.	Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle. 
class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


c = Car()
b = Bike()
bu = Bus()

c.start()
b.start()
bu.start()

#4.Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion. Override sound() in each class to display the appropriate sound.
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says: Roar")


d = Dog()
c = Cat()
co = Cow()
l = Lion()

d.sound()
c.sound()
co.sound()
l.sound()
#5.	Create a base class Notification with a method send(). Derive EmailNotification, SMSNotification, and PushNotification. Override send() to display the appropriate notification method.
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification")


e = EmailNotification()
s = SMSNotification()
p = PushNotification()

e.send()
s.send()
p.send()
#6.	Create a base class Student with a method calculate_grade(). Derive EngineeringStudent, MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.
class Student:
    def calculate_grade(self, marks):
        print("Calculating grade")


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            print("Engineering Grade: A")
        elif marks >= 60:
            print("Engineering Grade: B")
        elif marks >= 50:
            print("Engineering Grade: C")
        else:
            print("Engineering Grade: Fail")


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            print("Medical Grade: A")
        elif marks >= 65:
            print("Medical Grade: B")
        elif marks >= 50:
            print("Medical Grade: C")
        else:
            print("Medical Grade: Fail")


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            print("Management Grade: A")
        elif marks >= 55:
            print("Management Grade: B")
        elif marks >= 40:
            print("Management Grade: C")
        else:
            print("Management Grade: Fail")


e = EngineeringStudent()
m = MedicalStudent()
mg = ManagementStudent()

e.calculate_grade(72)
m.calculate_grade(82)
mg.calculate_grade(60)
#7.	Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount, CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently for each account type.
class BankAccount:
    def calculate_interest(self, amount):
        print("Calculating interest")


class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        print("Savings Account Interest:", amount * 5 / 100)


class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        print("Current Account Interest:", amount * 2 / 100)


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, amount):
        print("Fixed Deposit Interest:", amount * 7 / 100)


s = SavingsAccount()
c = CurrentAccount()
f = FixedDepositAccount()

s.calculate_interest(100000)
c.calculate_interest(100000)
f.calculate_interest(100000)

#8.	Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and HTMLReport. Override generate() in each class. Write a function that accepts any report object and calls generate().
class Report:
    def generate(self):
        print("Generating report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


p = PDFReport()
e = ExcelReport()
h = HTMLReport()

generate_report(p)
generate_report(e)
generate_report(h)
#9.	Create a class Distance with feet and inches. Overload the + operator to add two distance objects and display the result in normalized form.
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        if inches >= 12:
            feet = feet + inches // 12
            inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print("Distance:", self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2
d3.display()
#10.	Create a class Student containing the student's name and total marks. Overload the > and < operators to compare the marks of two students.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Sayali", 85)
s2 = Student("Anushka", 78)

print("Student 1 has greater marks:", s1 > s2)
print("Student 1 has smaller marks:", s1 < s2)
#11.	Create a class Product with product name and price. Overload the == and > operators to compare two products based on their prices.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 30000)

print("Prices are equal:", p1 == p2)
print("Product 1 is more expensive:", p1 > p2)
#12.	Develop an online shopping payment module using polymorphism. Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement its own make_payment() method. Demonstrate polymorphism using a common function.
class Payment:
    def make_payment(self):
        print("Making payment")


class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI")


class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Card")


class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet")


def process_payment(payment):
    payment.make_payment()


process_payment(UPIPayment())
process_payment(CardPayment())
process_payment(WalletPayment())
#13.	Create a base class Person with a method display_role(). Derive Student, Faculty, and Administrator. Override the method to display the respective role. Store all objects in a list and invoke the same method using a loop.
class Person:
    def display_role(self):
        print("I am a person")


class Student(Person):
    def display_role(self):
        print("I am a Student")


class Faculty(Person):
    def display_role(self):
        print("I am a Faculty")


class Administrator(Person):
    def display_role(self):
        print("I am an Administrator")


people = [Student(), Faculty(), Administrator()]

for person in people:
    person.display_role()
#14.	Create a base class Media with a method play(). Derive Audio, Video, and Podcast. Override play() according to the media type.
class Media:
    def play(self):
        print("Playing media")


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media = [Audio(), Video(), Podcast()]

for m in media:
    m.play()
#15.	Create a base class SmartDevice with methods turn_on() and turn_off(). Derive Light, Fan, AC, and TV. Override the methods according to each device.
class SmartDevice:
    def turn_on(self):
        print("Device is ON")

    def turn_off(self):
        print("Device is OFF")


class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()
