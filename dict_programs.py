#1.Create a dictionary containing student details such as roll number, name,
#department, and marks. Display all key-value pairs.
print("1.dictionary containing student details")
d={'rollno':21,'name':'Shreya','dept':'CSE','Marks':95}
print(d)


#2.Create a dictionary containing employee information and display the value
#associated with a specified key.
print("\n\n2.dictionary containing employee information")
employee = {
    "Name": "Rahul",
    "Age": 25,
    "Salary": 30000,
    "Department": "IT"
}
key = "Salary"
print("Value associated with", key, ":", employee[key])


#3.Create a dictionary of five products and their prices.
#Add a new product and price to the dictionary.
print("\n\n3.dictionary of five products")
products={'Smartphone':25000,'Laptop':75000,'Watch':2000,'earbuds':500,'powerbank':1500}
products['Fan']=3000
print(products)


#4.Create a dictionary containing student marks. Update the marks of a specified student.
print("\n\n4.Update the marks of a specified student")
marks={'s1':90,'s2':89,'s3':95,'s4':75,'s5':77}
marks['s4']=88
print(marks)


#5.Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
print("\n\n5.Update the marks of a specified student")
marks={'Karad':9000,'Kolhapur':15000,'koregaon':2500,'Kagal':5000}
del marks['Kagal']
print(marks)


#6.Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
print("\n\n6.dictionary containing employee information")
employee = {101:'Shreya',102:'Sayali',103:'Dipali',104:'Anushka'}
id=int(input("Enter id to search:"))
for i in employee.keys():
    if id==i:
        print("Found")
        break
else:
    print("Not Found")


#7.Create a dictionary containing student records and find the total number of key-value pairs.
print("")
stud = {101:'Shreya',102:'Sayali',103:'Dipali',104:'Anushka'}
count=1
for i in stud.keys():
    count+=1
print("Total records:",count)


"""8.Create a dictionary and display:
All keys 
All values 
All key-value pairs"""
print("\n\n8.display")
employee = {101:'Shreya',102:'Sayali',103:'Dipali',104:'Anushka'}
for i in employee.keys():
    print(i,end=",")
print()
for i in employee.values():
    print(i,end=",")
print()
for key, value in employee.items():
    print(key, ":", value)


# 9. Dictionary of programming languages and their creators
print("\n\n9. Dictionary of programming languages and their creators")
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for language, creator in languages.items():
    print(language, ":", creator)


# 10. Accept five student names and their marks and store them in a dictionary
print("\n\n10.Accept five student names and their marks")
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print("Student Dictionary:", students)



#11.Create a dictionary containing student names and marks.
#Find the student who has scored the highest marks.
print("\n\n11.Find the student who has scored the highest marks.")
stud={'Shreya':95,'Tanu':80,'Dipa':90,'Maitreyee':92,'Manasi':91}
key = max(stud, key=stud.get)
print(key, ":", stud[key])



#12.Create a dictionary containing student names and marks.
#Find the student with the lowest marks.
print("\n\n12.Find the student who has scored the lowest marks.")
stud={'Shreya':95,'Tanu':80,'Dipa':90,'Maitreyee':92,'Manasi':91}
key = min(stud, key=stud.get)
print(key, ":", stud[key])


#13.Create a dictionary containing student names and marks.
#Calculate the average marks of all students.
print("\n\n13.Calculate the average marks of all students")
stud={'Shreya':95,'Tanu':80,'Dipa':90,'Maitreyee':92,'Manasi':91}
avg=0
for key,vals in stud.items():
    avg+=vals
print(avg/len(stud))


#14.Accept a string from the user and create a dictionary containing each
#character and its frequency.
print("\n\n14.each character and its frequency")
s=input("Enter a String:")
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(freq)


#15.Accept a sentence and create a dictionary containing each word
#and the number of times it occurs.
print("\n\n15.each word and its frequency")
s=input("Enter a String:")
words=s.split()
freq={}
for i in words:
    freq[i]=freq.get(i,0)+1
print(freq)



#16.Create two dictionaries and merge them into a single dictionary.
print("16.Create two dictionaries and merge them into a single dictionary.")
d1={'s1':1,'s2':2,'s3':3}
d2={'s4':4,'s5':5}
d1.update(d2)
print("After Merging:",d1)


#17.Given two dictionaries, find the keys that are common to both dictionaries.
print("17.find the keys that are common to both dictionaries.")
d1={'s1':1,'s2':2,'s3':3,'s4':4}
d2={'s4':4,'s5':5}
for i in d1:
    for j in d2:
        if i==j:
            print(i,end=" ")


#18.Given two dictionaries, identify the values that are common to both dictionaries.
print("\n\n18.Given two dictionaries,identify values that are common to both dictionaries.")
d1={'s1':1,'s2':2,'s3':3,'s4':4}
d2={'s4':4,'s5':5}
for i in d1.values():
    for j in d2:
        if i==j:
            print(i,end=" ")


#19.Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
print("19. Remove duplicate values while retaining corresponding keys.")
d1 = {'s1':1, 's2':2, 's3':3, 's4':2, 's5':4}
new = {}
for key, value in d1.items():
    if value not in new.values():
        new[key] = value
print("After removing duplicate values:", new)


#20.Create a dictionary and display its elements in ascending order of keys.
print("20.Create a dictionary and display its elements in ascending order of keys.")
d = {'s3':3, 's1':1, 's4':4, 's2':2}
for key in sorted(d):
    print(key, ":", d[key])


#21.Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
print("\n\n21.dictionary containing numbers from 1 to 10 as keys and their squares as values")
d = {}
for i in range(1, 11):
    d[i] = i * i
print(d)



#22.Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
print("\n\n21.1 to 20 as keys and their squares as values(even only)")
d = {}
for i in range(1, 21):
    if i%2==0:
        d[i] = i * i
print(d)


#23.Given a list of numbers, create a dictionary containing each unique number and its frequency.
print("\n\n23.each unique number and its frequency")
s=[1,2,1,1,2,3,4,3,5,6]
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(freq)


#24.Create a dictionary containing integers from 1 to 10 and their cubes.
print("\n\n24.Create a dictionary containing integers from 1 to 10 and their cubes.")
d = {}
for i in range(1, 11):
    d[i] = i**3
print(d)



"""25.Create a dictionary containing student names and marks. Develop a program to:
Add a student 
Update marks 
Delete a student 
Search for a student 
Display all students 
Find the highest marks 
Calculate the average"""
print("\n\n25.find...")
students = {
    'Shreya': 95,
    'Tanu': 80,
    'Dipa': 90
}
name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks
print("Student added successfully.")

name = input("\nEnter student name to update marks: ")
if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks
    print("Marks updated successfully.")
else:
    print("Student not found.")

name = input("\nEnter student name to delete: ")
if name in students:
    del students[name]
    print("Student deleted successfully.")
else:
    print("Student not found.")

name = input("\nEnter student name to search: ")
if name in students:
    print(name, ":", students[name])
else:
    print("Student not found.")

print("\nAll Students:")
for name, marks in students.items():
    print(name, ":", marks)

highest = max(students.values())
print("\nHighest Marks:", highest)

average = sum(students.values()) / len(students)
print("Average Marks:", average)



"""
26.Create a dictionary containing employee names and salaries. Find:
Highest salary 
Lowest salary 
Average salary 
Employees earning more than ₹50,000"""
print("\n\n26.")
employee = {
    'Shreya': 60000,
    'Tanu': 45000,
    'Dipa': 75000,
    'Maitreyee': 55000,
    'Manasi': 40000
}

print("Highest Salary:", max(employee.values()))
print("Lowest Salary:", min(employee.values()))

average = sum(employee.values()) / len(employee)
print("Average Salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employee.items():
    if salary > 50000:
        print(name, ":", salary)



"""
27.Create a dictionary containing product names and quantities.
Perform:
Add a product 
Update quantity 
Delete a product 
Search for a product 
Display products with quantity below 10"""
print("\n\n27.")
product = {
    'Pen': 20,
    'Book': 15,
    'Pencil': 5,
    'Eraser': 8
}

name = input("Enter product name to add: ")
quantity = int(input("Enter quantity: "))
product[name] = quantity
print("Product added successfully.")

name = input("\nEnter product name to update: ")
if name in product:
    quantity = int(input("Enter new quantity: "))
    product[name] = quantity
    print("Quantity updated successfully.")
else:
    print("Product not found.")

name = input("\nEnter product name to delete: ")
if name in product:
    del product[name]
    print("Product deleted successfully.")
else:
    print("Product not found.")

name = input("\nEnter product name to search: ")
if name in product:
    print(name, ":", product[name])
else:
    print("Product not found.")

print("\nProducts with quantity below 10:")
for name, quantity in product.items():
    if quantity < 10:
        print(name, ":", quantity)




"""
28.Create a dictionary containing names and phone numbers.
Implement:
Add contact 
Search contact 
Update contact 
Delete contact 
Display all contacts"""
print("\n\n28.")
contacts = {
    'Shreya': '9876543210',
    'Tanu': '9876501234',
    'Dipa': '9876512345'
}

name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone
print("Contact added successfully.")

name = input("\nEnter contact name to search: ")
if name in contacts:
    print(name, ":", contacts[name])
else:
    print("Contact not found.")

name = input("\nEnter contact name to update: ")
if name in contacts:
    phone = input("Enter new phone number: ")
    contacts[name] = phone
    print("Contact updated successfully.")
else:
    print("Contact not found.")

name = input("\nEnter contact name to delete: ")
if name in contacts:
    del contacts[name]
    print("Contact deleted successfully.")
else:
    print("Contact not found.")

print("\nAll Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)




"""
29.Create a dictionary containing book IDs and book names.
Implement:
Add a book 
Search a book 
Remove a book 
Display all books 
Count total books"""
print("\n\n29.")
books = {
    101: 'Python',
    102: 'Java',
    103: 'C++'
}

book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name
print("Book added successfully.")

book_id = int(input("\nEnter book ID to search: "))
if book_id in books:
    print(book_id, ":", books[book_id])
else:
    print("Book not found.")

book_id = int(input("\nEnter book ID to remove: "))
if book_id in books:
    del books[book_id]
    print("Book removed successfully.")
else:
    print("Book not found.")

print("\nAll Books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

print("\nTotal Books:", len(books))




#30.Take a dictionary containing student names and their departments;
#create a new dictionary that groups students according to their department.
print("\n\n30.")
students = {
    'Shreya': 'CSE',
    'Tanu': 'IT',
    'Dipa': 'CSE',
    'Maitreyee': 'ENTC',
    'Manasi': 'IT'
}
grouped = {}
for name, department in students.items():
    if department not in grouped:
        grouped[department] = []
    grouped[department].append(name)
print("Students grouped by department:")

for department, names in grouped.items():
    print(department, ":", names)



#31.Take a list of words, create a dictionary where the key is the word length
#and the value is a list of words having that length.
print("\n\n31.")
words = ['cat', 'dog', 'apple', 'ball', 'sun', 'banana']
result = {}
for word in words:
    length = len(word)

    if length not in result:
        result[length] = []
    result[length].append(word)
print(result)


print("\n\n32.")
nums = [2, 7, 11, 15]
target = 9
d = {}
for num in nums:
    if target - num in d:
        print("Numbers:", target - num, "and", num)
        break
    d[num] = True


print("\n\n33.")
s = "swiss"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break



print("\n\n34.")
s = "swiss"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] > 1:
        print("First repeating character:", ch)
        break

    
print("\n\n35.")
paragraph = input("Enter a paragraph: ")
words = paragraph.split()
result = {}
for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1
print(result)
