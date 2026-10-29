#33. Lambda function to calculate square
square = lambda n: n * n

num = int(input("Enter a number: "))
print("Square =", square(num))

#34. Lambda function to calculate cube
cube = lambda n: n * n * n

num = int(input("Enter a number: "))
print("Cube =", cube(num))

#35. Lambda function to check even number
even = lambda n: n % 2 == 0

num = int(input("Enter a number: "))
print(even(num))

#36. Lambda function to find maximum of two numbers
maximum = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))

#37. Lambda function to calculate Simple Interest


simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest =", simple_interest(p, r, t))

#38. Generate squares using map() and lambda
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Squares =", squares)



#39. Generate cubes using map() and lambda
numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda x: x * x * x, numbers))

print("Cubes =", cubes)

#40. Sum corresponding elements of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = list(map(lambda x, y: x + y, list1, list2))

print("Sum =", result)


#41. Extract even numbers
numbers = [10, 15, 20, 25, 30, 35]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers =", even)

#42. Identify prime numbers using filter() and lambda
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13]

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

prime = list(filter(is_prime, numbers))

print("Prime numbers =", prime)


#43. Extract positive numbers
numbers = [-10, 5, -3, 8, 0, -2, 15]

positive = list(filter(lambda x: x > 0, numbers))

print("Positive numbers =", positive)

#44. Find numbers greater than 50
numbers = [20, 55, 40, 75, 90, 30, 60]

result = list(filter(lambda x: x > 50, numbers))

print("Numbers greater than 50 =", result)

#45. Find words having more than five characters
words = ["apple", "banana", "cat", "computer", "school", "pen"]

result = list(filter(lambda word: len(word) > 5, words))

print("Words =", result)

#46. Sort words according to their length
words = ["apple", "cat", "elephant", "dog", "banana"]

result = sorted(words, key=lambda word: len(word))

print("Sorted words =", result)


#47. Sort students according to marks
students = [
    ("Sayali", 85),
    ("Anushka", 72),
    ("Shreya", 90),
    ("Sanika", 78)
]

result = sorted(students, key=lambda student: student[1])

print("Students sorted by marks:")
for student in result:
    print(student)

#48. Sort employees according to salary
employees = [
    ("Rahul", 45000),
    ("Amit", 60000),
    ("Priya", 50000),
    ("Neha", 75000)
]

result = sorted(employees, key=lambda emp: emp[1])

print("Employees sorted by salary:")
for employee in result:
    print(employee)

#49. Student names and marks using functions and lambda
#a) Calculate average marks
#b) Filter students scoring above 75
#c) Sort students according to marks
students = [
    ("Sayali", 85),
    ("Anushka", 72),
    ("Shreya", 90),
    ("Sanika", 78),
    ("Deepali", 65)
]

# a) Calculate average
def average_marks(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)

print("Average marks =", average_marks(students))

# b) Students scoring above 75
above_75 = list(filter(lambda student: student[1] > 75, students))

print("\nStudents scoring above 75:")
for student in above_75:
    print(student)

# c) Sort according to marks
sorted_students = sorted(students, key=lambda student: student[1])

print("\nStudents sorted by marks:")
for student in sorted_students:
    print(student)

#50. Employee records using filter(), map() and sorted()
#a) Employees earning more than ₹50,000
#b) Increase salaries by 10%
#c) Sort employees according to salary
employees = [
    ("Rahul", "IT", 45000),
    ("Amit", "HR", 60000),
    ("Priya", "IT", 75000),
    ("Neha", "Finance", 50000)
]

# a) Salary more than 50000
high_salary = list(filter(lambda emp: emp[2] > 50000, employees))

print("Employees earning more than 50000:")
for emp in high_salary:
    print(emp)

# b) Increase salary by 10%
increased_salary = list(
    map(lambda emp: (emp[0], emp[1], emp[2] * 1.10), employees)
)

print("\nSalary after 10% increase:")
for emp in increased_salary:
    print(emp)

# c) Sort according to salary
sorted_employees = sorted(employees, key=lambda emp: emp[2])

print("\nEmployees sorted by salary:")
for emp in sorted_employees:
    print(emp)

#51. Products using functions and lambda
#a) Calculate total value
#b) Filter products costing more than ₹1,000
#c) Sort according to total value
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Pen Drive", 800, 2)
]

# a) Calculate total value
def total_value(product):
    return product[1] * product[2]

for product in products:
    print(product[0], "Total Value =", total_value(product))

# b) Products costing more than 1000
result = list(filter(lambda p: total_value(p) > 1000, products))

print("\nProducts costing more than 1000:")
for product in result:
    print(product)

# c) Sort according to total value
sorted_products = sorted(products, key=lambda p: total_value(p))

print("\nProducts sorted by total value:")
for product in sorted_products:
    print(product)

#52. Process words using functions, map(), filter() and lambda
#a) Find length of every word
#b) Extract words having more than five characters
#c) Sort words according to length
words = ["apple", "banana", "cat", "elephant", "school", "computer"]

# a) Find length of every word
lengths = list(map(lambda word: len(word), words))

print("Length of words =", lengths)

# b) Words having more than 5 characters
long_words = list(filter(lambda word: len(word) > 5, words))

print("\nWords having more than 5 characters:")
print(long_words)

# c) Sort according to length
sorted_words = sorted(words, key=lambda word: len(word))

print("\nWords sorted according to length:")
print(sorted_words)
