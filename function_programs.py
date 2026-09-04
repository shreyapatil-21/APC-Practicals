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



"""
24.Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
25.Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
26.Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
27.Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.
28.Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
29.Write a recursive function to search for an element in a sorted list using binary search.
30.Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
31.Check whether a string is a palindrome using recursion.
32.Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
Programs on Lambda Function
33.Write a lambda function to calculate the square of a given number.
34.Create a lambda function that returns the cube of a number.
35.Write a lambda function that returns True if a number is even and False otherwise.
36.Use a lambda function to find the maximum of two numbers.
37.Create a lambda function to calculate simple interest using principal, rate, and time.
38.Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
39.Use map() with lambda to calculate the cube of every element in a list.
40.Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
41.Take a list of integers, use filter() and lambda to extract all even numbers.
42.Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
43.Use filter() and lambda to extract positive numbers from a list.
44.Take a list of numbers, use filter() and lambda to find numbers greater than 50.
45.Take a list of words, use filter() and lambda to find words having more than five characters.
46.Take a list of words; sort them according to their length using lambda.
47.Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
48.Take employee records containing name and salary, sort them according to salary using lambda.
49.Take a list containing student names and marks, use functions and lambda expressions to:
a)Calculate average marks. 
b)Filter students scoring above 75. 
c)Sort students according to marks.
50.Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
a)Find employees earning more than ₹50,000. 
b)Increase salaries by 10%. 
c)Sort employees according to salary.
51.Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
a)Calculate total value of each product. 
b)Filter products costing more than ₹1,000. 
c)Sort products according to total value.
52.Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
a)Find the length of every word. 
b)Extract words having more than five characters. 
c)Sort words according to their length."""
