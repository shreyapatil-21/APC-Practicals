
# 1
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

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
r = Rectangle(10, 5)
t = Triangle(10, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())


# 2
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

    def stop(self):
        print("Car stops")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

    def stop(self):
        print("Bike stops")

class Bus(Vehicle):
    def start(self):
        print("Bus starts")

    def stop(self):
        print("Bus stops")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# 3
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)
print("Savings Balance:", s.balance)

c = CurrentAccount(20000)
c.deposit(5000)
c.withdraw(4000)
print("Current Balance:", c.balance)


# 4
from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0

class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 50

r = RestaurantOrder(500)
print("Restaurant Bill:", r.calculate_bill() + r.delivery_charge())

h = HomeDeliveryOrder(500)
print("Home Delivery Bill:", h.calculate_bill() + h.delivery_charge())


# 5
from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        return "In-Patient treatment"

class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        return "Out-Patient treatment"

class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        return "Emergency treatment"

patients = [InPatient(), OutPatient(), EmergencyPatient()]

for patient in patients:
    print("Treatment:", patient.treatment())
    print("Bill:", patient.calculate_bill())
    print()


# 6
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 10

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 5

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 20

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 50

distance = 100

bus = Bus()
train = Train()
taxi = Taxi()
flight = Flight()

print("Bus Fare:", bus.calculate_fare(distance))
print("Train Fare:", train.calculate_fare(distance))
print("Taxi Fare:", taxi.calculate_fare(distance))
print("Flight Fare:", flight.calculate_fare(distance))


# 7
from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass

class MCQQuestion(Question):
    def __init__(self, correct_answer, user_answer):
        self.correct_answer = correct_answer
        self.user_answer = user_answer

    def evaluate_answer(self):
        if self.correct_answer == self.user_answer:
            return "Correct"
        else:
            return "Wrong"

class TrueFalseQuestion(Question):
    def __init__(self, correct_answer, user_answer):
        self.correct_answer = correct_answer
        self.user_answer = user_answer

    def evaluate_answer(self):
        if self.correct_answer == self.user_answer:
            return "Correct"
        else:
            return "Wrong"

class DescriptiveQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self):
        if len(self.answer) >= 20:
            return "Answer Accepted"
        else:
            return "Answer Too Short"

mcq = MCQQuestion("A", "A")
tf = TrueFalseQuestion(True, False)
descriptive = DescriptiveQuestion(
    "Python is an object oriented programming language."
)

print("MCQ:", mcq.evaluate_answer())
print("True/False:", tf.evaluate_answer())
print("Descriptive:", descriptive.evaluate_answer())


# 8
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")

methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()


# 9
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass

class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")

class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")

class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")

services = [GoogleDrive(), Dropbox(), OneDrive()]

for service in services:
    service.upload_file()
    service.download_file()
    service.delete_file()
    print()


# 10
from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500

class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000

class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000

appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())
    print()
