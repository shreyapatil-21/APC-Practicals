#1.Write a function factorial(n) that accepts an integer and returns its factorial.
print("\n\n1.factorial")
n=int(input("Enter a number:"))
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print("Factorial:",fact(n))


#2.Write a function check_even_odd(n) that determines whether a given number is even or odd.
print("\n\n2.Even odd")
n=int(input("Enter a number:"))
def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(n," is",evenodd(n))


#3.Define a function that accepts two numbers and returns the greater number.
print("\n\n3.Find greatest among 2 numbers")
n1=int(input("Enter a number1:"))
n2=int(input("Enter a number2:"))
def greatest(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
print(greatest(n1,n2)," is greatest")


#4.Create a function simple_interest(p, r, t) to calculate simple interest.
print("\n\n4.Find simple interest")
p=float(input("Enter Principle amount:"))
r=int(input("Enter rate:"))
t=int(input("Enter time:"))
def simple_interest(p, r, t):
    return (p*r*t)/100
print("Interest:",simple_interest(p, r, t))


#5.Write a function is_prime(n) that returns True if a number is prime;
#otherwise, returns False.
print("\n\n5.check number is prime or not")
n=int(input("Enter number:"))
def is_prime(n):
    if n==0 or n==1:
        print("Not prime")
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
print(is_prime(n))


#6.Define a function to calculate the area of a circle using its radius.
print("\n\n6.calculate the area of a circle")
r=int(input("Enter radius:"))
def calc(n):
    return 3.14*r*r
print("Area of circle:",calc(r))


#7.Write a function that accepts n and returns the sum of the first n natural numbers.
print("\n\n7.sum of the first n natural numbers")
n=int(input("Enter number:"))
def calc(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print("Sum of natural numbers::",calc(n))



#8.Create a function power(base, exponent) to calculate the value of base raised to exponent.
print("\n\n8.power of number")
base=int(input("Enter base:"))
exponent=int(input("Enter base:"))
def power(base, exponent):
    return base**exponent
print("power of number:",power(base, exponent))


#9.Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
print("\n\n9.Largest number")
ls=[100,23,678,334,78,454]
def largest(ls):
    large=ls[0]
    for i in ls:
        if i>large:
            large=i    
    return large
print("Large number:",largest(ls))


#10.Define a function that accepts a string and returns the number of vowels present in it.
print("\n\n10.number of vowels present")
s=input("Enter string:")
def vowel_count(s):
    count=0
    for i in s:
       if i in 'aeiou':
           count+=1
    return count
print("Vowel Count:",vowel_count(s))



#11.Write a function that accepts a string and returns its reverse.
print("\n\n11.Write a function that accepts a string and returns its reverse.")
s=input("Enter string:")
def reverse(s):
    return s[::-1]
print("Reversed:",reverse(s))


#12.Create a function that checks whether a given string or number is a palindrome.
print("\n\n12.String palindrome or not")
s=input("Enter string:")
def palindrome(s):
    res=""
    for ch in s:
        res=ch+res
    if s==res:
        return "Palindrome"
    else:
        return "not Palindrome"
print(palindrome(s))


#13.Write a function that accepts a list of numbers and returns their average.
print("\n\n13.accepts a list of numbers and returns their average.")
ls=[]
def average(ls):
    num=5
    for ch in range(num):
        n=int(input("Enter number:"))
        ls.append(n)
    return sum(ls)/num
print(average(ls))


#14.Define a function that accepts a list and an element and returns the number
#of times that element occurs.
print("\n\n14.Frequency of numbers")
ls=[1,2,1,3,2,4,5,5]
def frequency(ls):
    freq={}
    for ch in ls:
        freq[ch]=freq.get(ch,0)+1
    for i in freq:
        return freq
print(frequency(ls))


#15.Write a function that accepts a list and returns a new list containing only unique elements.
print("\n\n15.unique elements")
ls=[1,2,1,3,2,4,5,5]
def unique(ls):
    freq={}
    unique=[]
    for ch in ls:
        freq[ch]=freq.get(ch,0)+1
    for i in freq:
        if freq[ch]==1:
            unique.append(ch)
    return unique
print(unique(ls))


#16.Create a function to find the second-largest number in a list.
print("\n\n16.Second Largest number")
ls=[100,23,678,334,78,454]
def largest(ls):
    large=ls[0]
    second=ls[0]
    for i in ls:
        if i>large:
            second=large
            large=i
        elif i>second and i!=large:
            second=i
    return second
print("second Largest number:",largest(ls))


#17.Write a function that accepts n and returns the first n Fibonacci numbers.
print("\n\n17.first n Fibonacci numbers")
n=int(input("Enter number:"))
def fibbonacci_no(n):
    n1=0
    n2=1
    print(n1,n2)
    for i in range(2,n+1):
        n3=n1+n2
        print(n3)
fibbonacci_no(n)


#18.Create a function that accepts marks in five subjects and returns the student's percentage and grade.
print("\n\n18.Student percentage")
def per(sub1,sub2,sub3,sub4,sub5):
    total=sub1+sub2+sub3+sub4+sub5
    per=(total*100)/500
    return per
sub1,sub2,sub3,sub4,sub5=int(input("Enter Marks of 5 subjects:")).split()
print("Percentage is:",per(sub1,sub2,sub3,sub4,sub5))



#19.Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
print("\n\n19.electricity bill")
units=int(input("Enter Units consumed:"))
rate=int(input("Enter Rate per unit:"))
fixed_charge=int(input("Enter fixed charges:"))
tax=int(input("Enter tax amount:"))
def calc(units,rate,fixed_charge,tax):
    bill=units*rate+fixed_charge+tax
    return bill
print("Bil amount:",calc(units,rate,fixed_charge,tax))


#20.Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
print("\n\n20.Gross salary")
salary=float(input("Enter Basic Salary:"))
HRA=int(input("Enter HRA:"))
DA=int(input("Enter DA:"))
Allowances=int(input("Enter Allowances:"))
bonus=int(input("Enter bonus amount:"))
overtime=int(input("Enter overtime:"))
def calc(salary,HRA,DA,Allowances,bonus,overtime):
    gross=salary+HRA+DA,Allowances+bonus+overtime
    return gross
print("Gross Salary:",calc(salary,HRA,DA,Allowances,bonus,overtime))


#21.Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
print("\n\n19.grocery bill")
def total_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    discount_amount = total * discount / 100
    final_bill = total - discount_amount
    return final_bill

prices = [100, 200, 50]
quantities = [2, 1, 3]
discount = 10
print("Total bill after discount:", total_bill(prices, quantities, discount))


#22.Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
ls=[1,3,4,6,8,56,354,76,2]
def cacl(ls):
    print("Sum:",sum(ls))
    print("Maximum:",max(ls))
    print("Minimum:",min(ls))
    print("Average:",sum(ls)/len(ls))
calc(ls)


#23.Write a program using separate functions to process student records containing name,
#roll number, and marks in five subjects.
#Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks)/5

def calculate_grade(percentage):
    if percentage>=90:
        return "A+"
    elif percentage>=80:
        return "A"
    elif percentage>=70:
        return "B"
    elif percentage>=60:
        return "C"
    elif percentage>=50:
        return "D"
    else:
        return "F"

def class_average(students):
    total=0
    for student in students:
        total+=calculate_percentage(student["marks"])
    return total/len(students)

def highest_scorer(students):
    return max(students,key=lambda x:calculate_total(x["marks"]))

def lowest_scorer(students):
    return min(students,key=lambda x:calculate_total(x["marks"]))

students=[
    {"name":"Shreya","roll":1,"marks":[85,90,78,88,92]},
    {"name":"Sayali","roll":2,"marks":[75,80,70,82,78]},
    {"name":"Dipali","roll":3,"marks":[92,95,90,94,96]}
]

for student in students:
    total=calculate_total(student["marks"])
    percentage=calculate_percentage(student["marks"])
    grade=calculate_grade(percentage)
    print("\nName:",student["name"])
    print("Roll Number:",student["roll"])
    print("Total:",total)
    print("Percentage:",percentage)
    print("Grade:",grade)

print("\nClass Average:",class_average(students))

high=highest_scorer(students)
print("Highest Scorer:",high["name"],"-",calculate_total(high["marks"]))

low=lowest_scorer(students)
print("Lowest Scorer:",low["name"],"-",calculate_total(low["marks"]))



# Create functions for deposit, withdrawal, balance enquiry, and transaction history.

balance = 1000
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient Balance")

def enquiry():
    print("Balance =", balance)

def transaction_history():
    print("\nTransaction History")
    for i in history:
        print(i)

deposit(500)
withdraw(300)
withdraw(2000)
enquiry()
transaction_history()



# Create functions to add books, issue books, return books, search books, and display available books.

books = {}

def add_book(name):
    books[name] = "Available"

def issue_book(name):
    if name in books and books[name] == "Available":
        books[name] = "Issued"
    else:
        print("Book not available")

def return_book(name):
    if name in books:
        books[name] = "Available"

def search_book(name):
    if name in books:
        print(name, ":", books[name])
    else:
        print("Book not found")

def display_books():
    print("\nAvailable Books")
    for book, status in books.items():
        if status == "Available":
            print(book)

add_book("Python")
add_book("Java")
add_book("C Programming")

issue_book("Python")
return_book("Python")
search_book("Java")
display_books()


# Develop a modular program using functions to calculate electricity bills
# using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_energy_charge(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5

def fixed_charge():
    return 100

def tax(amount):
    return amount * 0.05

def discount(amount):
    if amount > 1000:
        return amount * 0.10
    return 0

units = int(input("Enter units consumed: "))

energy = calculate_energy_charge(units)
fixed = fixed_charge()
subtotal = energy + fixed
gst = tax(subtotal)
disc = discount(subtotal)

final_bill = subtotal + gst - disc

print("Energy Charge =", energy)
print("Fixed Charge =", fixed)
print("GST =", gst)
print("Discount =", disc)
print("Final Bill =", final_bill)

# Create functions to calculate consultation charges, laboratory charges,
# medicine charges, room charges, and final bill.
# Apply discounts based on patient category.

def consultation():
    return float(input("Enter consultation charge: "))

def laboratory():
    return float(input("Enter laboratory charge: "))

def medicine():
    return float(input("Enter medicine charge: "))

def room():
    return float(input("Enter room charge: "))

def discount(total, category):
    if category.lower() == "senior":
        return total * 0.20
    elif category.lower() == "staff":
        return total * 0.30
    else:
        return 0

c = consultation()
l = laboratory()
m = medicine()
r = room()

category = input("Enter patient category (General/Senior/Staff): ")

total = c + l + m + r
dis = discount(total, category)
final = total - dis

print("Total Bill =", total)
print("Discount =", dis)
print("Final Bill =", final)

# Implement functions to add/remove products, calculate subtotal,
# apply coupon discounts, calculate GST, and generate the final invoice.

cart = []

def add_product(name, price):
    cart.append((name, price))

def remove_product(name):
    global cart
    cart = [item for item in cart if item[0] != name]

def subtotal():


    return sum(price for name, price in cart)

def coupon(total):
    if total >= 1000:
        return total * 0.10
    return 0

def gst(total):
    return total * 0.18

add_product("Mouse", 500)
add_product("Keyboard", 700)
add_product("USB", 300)

remove_product("USB")

sub = subtotal()
dis = coupon(sub)
tax = gst(sub - dis)

final = sub - dis + tax

print("Subtotal =", sub)
print("Discount =", dis)
print("GST =", tax)
print("Final Invoice =", final)

# Write a recursive function to search for an element
# in a sorted list using binary search.

def binary_search(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)

# Convert a decimal number into binary using recursion
# without using Python's built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter decimal number: "))

if num == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(num))


# Check whether a string is a palindrome using recursion.

def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

string = input("Enter a string: ")

if palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")

# Create separate functions for addition, subtraction,
# multiplication, and division.
# Pass these functions as arguments to another function called calculate().

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

def calculate(fun, a, b):
    return fun(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", calculate(addition, a, b))
print("Subtraction =", calculate(subtraction, a, b))
print("Multiplication =", calculate(multiplication, a, b))
print("Division =", calculate(division, a, b))

# Write a lambda function to calculate the square of a given number.

square = lambda x: x * x

num = int(input("Enter a number: "))
print("Square =", square(num))

# Create a lambda function that returns the cube of a number.

cube = lambda x: x ** 3

num = int(input("Enter a number: "))
print("Cube =", cube(num))
Program
# Write a lambda function that returns True if a number is even and False otherwise.

even = lambda x: x % 2 == 0

num = int(input("Enter a number: "))
print(even(num))

# Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))
Program
# Create a lambda function to calculate simple interest
# using principal, rate, and time.

simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest =", simple_interest(p, r, t))
Program
# Take a list of numbers, use map() and a lambda function
# to generate a list containing their squares.

numbers = list(map(int, input("Enter numbers: ").split()))

square = list(map(lambda x: x * x, numbers))

print(square)

# Use map() with lambda to calculate the cube of every element in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

cube = list(map(lambda x: x ** 3, numbers))

print(cube)

# Take two lists of numbers, use map() and lambda to create
# a third list containing the sum of corresponding elements.

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda a, b: a + b, list1, list2))

print(result)

# Take a list of integers, use filter() and lambda to extract all even numbers.

numbers = list(map(int, input("Enter numbers: ").split()))

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


# Take a list of integers, use filter() with lambda to identify prime numbers.

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers: ").split()))

primes = list(filter(lambda x: prime(x), numbers))

print(primes)

# Use filter() and lambda to extract positive numbers from a list.

numbers = list(map(int, input("Enter numbers: ").split()))

positive = list(filter(lambda x: x > 0, numbers))

print(positive)


# Take a list of numbers, use filter() and lambda to find numbers greater than 50.

numbers = list(map(int, input("Enter numbers: ").split()))

result = list(filter(lambda x: x > 50, numbers))

print(result)


# Take a list of words, use filter() and lambda to find words having more than five characters.

words = input("Enter words: ").split()

result = list(filter(lambda x: len(x) > 5, words))

print(result)


# Take a list of words; sort them according to their length using lambda.

words = input("Enter words: ").split()

words.sort(key=lambda x: len(x))

print(words)


# Take a list of tuples containing student names and marks,
# sort the students according to their marks using lambda.

students = [("Amit", 78), ("Neha", 92), ("Riya", 65), ("Raj", 85)]

students.sort(key=lambda x: x[1])

print(students)
# Take employee records containing name and salary,
# sort them according to salary using lambda.

employees = [("Amit", 45000), ("Neha", 60000), ("Raj", 52000)]

employees.sort(key=lambda x: x[1])

print(employees)


# Take a list containing student names and marks.
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.

students = [("Amit", 78), ("Neha", 92), ("Raj", 65), ("Riya", 85)]

average = sum(map(lambda x: x[1], students)) / len(students)

above75 = list(filter(lambda x: x[1] > 75, students))

sorted_students = sorted(students, key=lambda x: x[1])

print("Average =", average)
print("Above 75 =", above75)
print("Sorted =", sorted_students)


# Take employee records containing name, department, and salary.
# a) Find employees earning more than ₹50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.

employees = [
    ("Amit", "HR", 45000),
    ("Neha", "IT", 70000),
    ("Raj", "Sales", 55000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

updated_salary = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))

sorted_salary = sorted(employees, key=lambda x: x[2])

print("Salary > 50000 =", high_salary)
print("Updated Salary =", updated_salary)
print("Sorted =", sorted_salary)


# Take a list of products with names, prices, and quantities.
# a) Calculate total value of each product.
# b) Filter products costing more than ₹1000.
# c) Sort products according to total value.

products = [
    ("Pen", 20, 50),
    ("Book", 200, 10),
    ("Bag", 1200, 2)
]

total_value = list(map(lambda x: (x[0], x[1] * x[2]), products))

costly = list(filter(lambda x: x[1] > 1000, products))

sorted_products = sorted(products, key=lambda x: x[1] * x[2])

print("Total Value =", total_value)
print("Costly Products =", costly)
print("Sorted =", sorted_products)

# Write a program using functions, map(), filter(), and lambda expressions
# to process a list of words.
# a) Find the length of every word.
# b) Extract words having more than five characters.
# c) Sort the words according to their length.

words = input("Enter words: ").split()

lengths = list(map(lambda x: len(x), words))

long_words = list(filter(lambda x: len(x) > 5, words))

sorted_words = sorted(words, key=lambda x: len(x))

print("Lengths =", lengths)
print("Words > 5 characters =", long_words)
print("Sorted =", sorted_words)

