
# 1
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()


s1 = Student(101, "Rahul", [80, 75, 90, 85, 88])
s2 = Student(102, "Priya", [90, 85, 92, 88, 95])

s1.display()
s2.display()


# 2
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.calculate_gross())
        print()


e1 = Employee(101, "Amit", 30000)
e1.display()


# 3
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())
print()


# 4
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(7)

print("Area:", c.area())
print("Circumference:", c.circumference())
print()


# 5
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


b1 = Book(1, "Python Basics", "John", 400)
b2 = Book(2, "Java Programming", "James", 500)
b3 = Book(3, "Data Science", "David", 600)

b1.display()
b2.display()
b3.display()


# 6
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.50
        elif self.units <= 200:
            bill = (100 * 1.50) + ((self.units - 100) * 2.50)
        elif self.units <= 300:
            bill = (100 * 1.50) + (100 * 2.50) + ((self.units - 200) * 4)
        else:
            bill = (100 * 1.50) + (100 * 2.50) + (100 * 4) + ((self.units - 300) * 5)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())
        print()


bill = ElectricityBill(1001, "Rahul", 250)
bill.display()


# 7
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)

phone.display()
print("Price after 10% discount:", phone.discount_price(10))
print()


# 8
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee


p = Patient(101, "Rohan", 25, "Fever", 500)

p.display()
print("Total Bill:", p.total_bill(1000))
print()


# 9
class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(12345, "Rahul", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.account_details()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")


# 10
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self, days):
        if not self.availability:
            self.availability = True
            charge = self.rental_rate * days
            print("Vehicle returned successfully")
            print("Rental Charge:", charge)
        else:
            print("Vehicle was not rented")


v = Vehicle("MH12AB1234", "Honda City", 2000)

v.rent()
v.return_vehicle(3)
print()


# 11
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart")
                return
        print("Product not found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        return total

    def display(self):
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Pen", 50)
cart.add_product("Book", 200)
cart.add_product("Bag", 500)

cart.remove_product("Pen")
cart.display()

del cart


# 12
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill including tax:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Priya", "Pizza", 2, 300)

order.display()

del order


# 13
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed")


student = StudentResult("Rahul", [85, 90, 78, 88, 92])

student.display()

del student

