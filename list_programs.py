#List Programs

#1.Write a Python program to create a list of five fruits and display the list.
print("1.list of five fruits")
fruits=['Apple','Banana','Orange','chiku','pinapple']
print(fruits)


#2.Create a list of five integers. Display:
#First element,Last element,Third element
print("\n\n2.list of five numbers")
list1=[1,2,3,4,5]
print("Original:",list1)
print("First Element:",list1[0])
print("Second Element:",list1[1])
print("Third Element:",list1[2])


#3.Create a list of colors.
#Replace the third color with another color and display the updated list.
print("\n\n3.list of colors")
list1=['Red','Blue','Black','Yellow','Pink']
print("Original:",list1)
list1[2]='White'
print("After Updating:",list1)


#4.Create a list of numbers. Add:
print("\n\n4.Create a list of numbers. Add:")
ls=[1,2,3,4,5]
print("Original:",ls)
ls.append(6)
ls.insert(0,0)
ls.insert(4,7)
print("After Inserting:",ls)

#5.Create a list of student names. Remove:
print("\n\n5.Create a list of student names. Remove:")
ls=['priya','Manali','Prachi','Shreya','Dipali','sayali']
print("Original:",ls)
del ls[0]
ls.pop()
ls.remove('Prachi')
print("After Removing:",ls)


#6.Write a program to find the largest and smallest number in a list
#without using max() or min().
print("\n\n6.find the largest and smallest number in a list")
ls=[70,10,5,15,100,99]
smallest=ls[0]
largest=ls[0]
for i in range(len(ls)):
    if ls[i]<smallest:
        smallest=ls[i]
    if ls[i]>largest:
        largest=ls[i]
print("Smallest Element:",smallest)
print("Largest Element:",largest)


#7.Accept 10 numbers from the user and store them in a list. Calculate:SumAverage
print("\n\n7. Calculate:Sum and Average")
n = 10
total = 0
ls = []
for i in range(n):
    num = int(input())
    ls.append(num)
    total += num

print("\nNumbers:", ls)
print("Sum:", total)
print("Average:", total / n)
    

#8.Store 15 integers in a list. Count how many numbers are:Even and Odd
print("\n\n8. Calculate count of even odd")
ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even,odd=0,0
for i in ls:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("\nNumbers:", ls)
print("Even count:", even)
print("Odd count:", odd)


#9.Create a list of cities. Ask the user to enter a city name and check whether
#it exists in the list.
print("\n\n9.Check city exist or not")
ls=['Karad','Koregaon','Kodoli','Kolhapur','Bawada']
city=input("Enter city to find:")
for i in ls:
    if i == city:
        print("Exist")
        break
else:
    print("Not Exist")


#10.Write a program to reverse a list without using the reverse() method.
print("\n\n10.Write a program to reverse a list")
lst=['Karad','Koregaon','Kodoli','Kolhapur','Bawada']
res=[]
for i in range(len(lst)-1,-1,-1):
    res.append(lst[i])
print(res)


"""11.Create a list of 10 numbers and display:
First 5 elements 
Last 5 elements 
Middle 4 elements 
Alternate elements
Reverse list using slicing"""

print("\n\n11.List Operations")
ls=[1,2,3,4,5,6,7,8,9,10]
print(ls[:5])
print(ls[5:])
print(ls[2:6])
print(ls[::2])
print(ls[::-1])


#12.Display all elements present at even index positions.
print("\n\n12.Display all elements present at even index positions.")
ls=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(ls)):
    if i%2!=0:
        print(ls[i],end=" ")
    

"""13.Accept 10 numbers and sort them in:
Ascending order 
Descending order"""
print("\n\n13.SOrting")
n = 10
ls=[67,34,5,23,12,7,8,9,45,56]
print("Original List:", ls)
ls.sort()
print("Ascending Order:", ls)
ls.sort(reverse=True)
print("Descending Order:", ls)


#14.Create a list containing duplicate values and display only unique elements.
print("\n\n14.display only unique elements.")
ls=[1,1,2,3,4,2,3]
unique=[]
for i in ls:
    if i not in unique:
        unique.append(i)
    else:
        pass
print("unique elements in list:",unique)



#15.Find the second largest element in a list.
print("\n\n15. Find the second largest element in a list.")
ls = [12, 45, 78, 34, 90, 56, 23, 67, 89, 11]
largest,second_largest = ls[0],ls[0]
for i in range(1, len(ls)):
    if ls[i] > largest:
        second_largest = largest
        largest = ls[i]
    elif ls[i] > second_largest and ls[i] != largest:
        second_largest = ls[i]

print("List:", ls)
print("Largest Element:", largest)
print("Second Largest Element:", second_largest)



#16.Create a nested list storing:
# Student Name
# Roll Number
# Marks
# Display all student details.

print("\n\n16. Create a nested list storing Student Name, Roll Number and Marks.")
students = [
    ["Shreya",101,85],
    ["Rahul",102,90],
    ["Priya",103,78]
]
print("Name\tRoll No\tMarks")
for i in students:
    print(i[0],"\t",i[1],"\t",i[2])


#17.Create two 3 × 3 matrices using nested lists and perform matrix addition.
print("\n\n17. Create two 3 × 3 matrices and perform matrix addition.")
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]]
C = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Matrix A")
for i in A:
    print(i)
print("Matrix B")
for i in B:
    print(i)
print("Addition Matrix")
for i in C:
    print(i)


#18.Create a shopping cart using a list.
# Perform:
# Add item
# Remove item
# Search item
# Display cart
# Count total items
print("\n\n18. Shopping Cart")
cart = ["Milk","Bread","Eggs"]
print("Original Cart:",cart)
cart.append("Butter")
print("After Adding:",cart)
cart.remove("Bread")
print("After Removing:",cart)
item = "Milk"
if item in cart:
    print(item,"Found")
else:
    print(item,"Not Found")
print("Shopping Cart:",cart)
print("Total Items:",len(cart))


#19.Store names of students present in class.
# Display:
# Total students
# Search a student's attendance
# Add a new student
# Remove an absent student
print("\n\n19. Student Attendance")
students = ["Shreya","Rahul","Priya","Amit"]
print("Students:",students)
print("Total Students:",len(students))
name = "Rahul"
if name in students:
    print(name,"is Present")
else:
    print(name,"is Absent")
students.append("Neha")
print("After Adding:",students)
students.remove("Amit")
print("After Removing:",students)


#20.Create a list of books.
# Implement:
# Add a new book
# Search a book
# Remove a book
# Display all books
# Count total books
print("\n\n20. Book List")
books = ["Python","Java","C","DBMS"]
print("Books:",books)
books.append("AI")
print("After Adding:",books)
book = "Python"
if book in books:
    print(book,"Found")
else:
    print(book,"Not Found")
books.remove("C")
print("After Removing:",books)
print("Display Books:",books)
print("Total Books:",len(books))
    


#21.Accept two lists and merge them into a single list.
print("\n\n21. Accept two lists and merge them into a single list.")
list1 = [10,20,30,40]
list2 = [50,60,70,80]
merged = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", merged)


#22.Find common elements between two lists.
print("\n\n22. Find common elements between two lists.")
list1 = [10,20,30,40,50]
list2 = [30,40,50,60,70]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common)


#23.Count the frequency of each element in a list.
print("\n\n23. Count the frequency of each element in a list.")
lst = [10,20,10,30,20,10,40,30]
checked = []
print("List:", lst)
for i in lst:
    if i not in checked:
        print(i, ":", lst.count(i))
        checked.append(i)


#24.Rotate a list:
# Left by one position
# Right by one position

print("\n\n24. Rotate a list.")

lst = [10,20,30,40,50]

left = lst[1:] + [lst[0]]
right = [lst[-1]] + lst[:-1]

print("Original List:", lst)
print("Left Rotation:", left)
print("Right Rotation:", right)


#25.Remove all duplicate elements while preserving the original order.

print("\n\n25. Remove all duplicate elements while preserving the original order.")

lst = [10,20,10,30,20,40,50,30,60]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("Original List:", lst)
print("List Without Duplicates:", new_list)



#26.Store marks of 20 students in a list and determine:
# Highest marks
# Lowest marks
# Average marks
# Number of students scoring above average
# Number of students scoring below average

print("\n\n26. Store marks of 20 students.")
marks = [45,67,89,90,56,78,88,92,65,73,55,61,80,84,76,95,48,69,71,87]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Marks:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)


#27.Store salaries of employees and determine:
# Highest salary
# Lowest salary
# Average salary
# Employees earning above ₹50,000
# Employees earning below ₹30,000

print("\n\n27. Store salaries of employees.")

salary = [25000,45000,55000,60000,28000,72000,35000,52000]

print("Salaries:", salary)
print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))
print("Average Salary:", sum(salary) / len(salary))

print("Employees earning above ₹50000:")
for i in salary:
    if i > 50000:
        print(i)

print("Employees earning below ₹30000:")
for i in salary:
    if i < 30000:
        print(i)


#28.Store scores of a batsman in 10 matches and calculate:
# Highest score
# Lowest score
# Total runs
# Average runs
# Number of centuries (>=100)
# Number of half-centuries (50–99)

print("\n\n28. Store scores of a batsman.")

scores = [45,120,80,30,150,60,99,110,40,75]

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

century = 0
half_century = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half_century += 1

print("Scores:", scores)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half Centuries:", half_century)


#29.Store the temperature of 30 days and determine:
# Hottest day
# Coldest day
# Average temperature
# Days above average temperature
# Days below average temperature

print("\n\n29. Store the temperature of 30 days.")
temp = [30,31,32,33,34,35,36,29,28,30,31,33,34,35,36,37,38,32,31,30,29,28,34,35,36,37,33,32,31,30]

average = sum(temp) / len(temp)

above = 0
below = 0

for i in temp:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Temperatures:", temp)
print("Hottest Day:", max(temp))
print("Coldest Day:", min(temp))
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)


#30.Store patient names and ages using lists.
# Perform:
# Add a patient
# Delete a patient
# Search a patient
# Display all patients
# Count total patients

print("\n\n30. Store patient names and ages.")

names = ["Amit", "Rahul", "Priya"]
ages = [25, 30, 22]

names.append("Neha")
ages.append(28)

print("After Adding:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

index = names.index("Rahul")
names.pop(index)
ages.pop(index)

print("\nAfter Deleting:")
for i in range(len(names)):
    print(names[i], "-", ages[i])
search = "Priya"
if search in names:
    print("\nPatient Found")
else:
    print("\nPatient Not Found")
print("\nAll Patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total Patients:", len(names))













