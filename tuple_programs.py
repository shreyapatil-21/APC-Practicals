#tuple
#1.Write a Python program to create a tuple of five integers and display it.
print("1.create a tuple of five integers")
tup=(1,2,3,4,5)
print(tup)


"""2.Create a tuple containing five city names. Display:
First city 
Last city 
Third city"""
print("\n\n2.tuple containing five city names.")
tup=('Karad','Satara','Kolhapur','Bawada','Pune')
print("First City:",tup[0])
print("Second City:",tup[1])
print("Third City:",tup[2])



#3.Create a tuple of student names and display the total number of students using the len() function.
print("\n\n3.total number of students using the len()")
tup=('Shreya','Manali','Vaishnavi','Dipali','Anushka')
print("Total Students:",len(tup))



#4.Create a tuple of colors. Check whether a given color exists in the tuple
print("\n\n4.Create a tuple of colors.")
tup=('Blue','White','Pink','Red','Yellow')
color=input("Enter Color to search:").title()
for i in tup:
    if i==color:
        print("Exist")
    else:
        print("Not Exist")
        break



#5.Create a tuple of fruits and display each fruit using a loop.
print("\n\n5.display each fruit")
tup=('Orange','Banana','Mango','Cherry','Chiku')
for ele in tup:
    print(ele,end=" ")



#6.Create a tuple with repeated numbers and count how many times a particular number appears.
print("\n\n6.element frequency:")
tup=(1,5,4,3,2,2,5,1,1,6)
freq={}
for i in tup:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    print(i,':',freq[i])



#7.Create a tuple of employee IDs and find the index of a given ID.
print("\n\n7.tuple of employee IDs and find the index of a given ID.")
tup=(101,102,103,104,105,106,107,108,109,110)
id=int(input("Enter ID:"))
print("Index of given ID:",tup.index(id))



#8.Create two tuples of numbers and concatenate them into a single tuple.
print("\n\n8.Concatinate 2 tuples into one")
tup1=(1,2,3,4)
tup2=(5,6,7,8)
tup3=tup1+tup2
print("Tuple after concatenation:",tup3)


#9.Create a tuple containing three elements and repeat it four times.
print("\n\n9.Repeatation of tuple elements:")
tup=(1,2,3)
print("Repeatation:",tup*4)


"""10.Create a tuple of 10 numbers and display:
First five elements 
Last five elements 
Middle four elements 
Alternate elements 
Reverse tuple"""
print("\n\n10.program")
tup=(1,2,3,4,5,6,7,8,9,10)
print("First five elements:",tup[:5])
print("Last five elements",tup[5:])
print("Middle five elements",tup[1:5])
print("Alternate elements",tup[::2])
print("Reverse tuple",tup[::-1])



#11.Convert a tuple into a list and add a new element.
print("11.Convert a tuple into a list and add a new element.")
tup=(1,2,3,4,5)
ls=list(tup)
ls.append(6)
print(ls)


#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple.
print("\n\n12.convert the list into a tuple")
ls=[]
for i in range(5):
    n=int(input("Enter number:"))
    ls.append(n)
tup=tuple(ls)
print(tup)


#13.Modify a tuple by converting it into a list and then back into a tuple.
print("\n\n13.Modify a tuple by converting it into a list and then back into a tuple.")
tup=(10,20,30)
ls=list(tup)
ls.extend([40,50])
tup=tuple(ls)
print(tup)


#14.Create a tuple and delete it completely.
print("\n\n14.Create a tuple and delete it completely.")
tup=(10,20,30)
del tup
print("deleted successfully")


#15.Create a nested tuple containing student details and display each record.
print("\n\n15.Create a nested tuple containing student details and display each record.")
tup=((101,'Shreya'),(102,'Dipali'),(103,'Sayali'),(104,'Vaishu'))
for i in tup:
    print(i)


#16.Store ten numbers in a tuple and calculate their sum.
print("\n\n16.Store ten numbers in a tuple and calculate their sum.")
tup=(10,12,14,15,16,17,18,19,20,21)
print("Sum is:",sum(tup))


#17.Find the largest and smallest number in a tuple without using max() and min().
print("\n\n17.Find the largest and smallest number in a tuple without using max() and min().")
tup=(56,34,2,67,22,89,100)
small=tup[0]
large=tup[0]
for i in tup:
    if i<small:
        small=i
    elif i>large:
        large=i
print("Smallest Element:",small)
print("Largest Element:",large)


#18.Calculate the average of elements stored in a tuple.
print("\n\n18.Calculate the average of elements stored in a tuple.")
tup=(56,34,2,67,22,89,100)
print("Average of Elements:",sum(tup)/len(tup))


"""19.Store 15 integers in a tuple and count:
Even numbers 
Odd numbers"""
print("\n\n19.Count Even and odd Elements")
tup=(56,34,2,67,22,89,100,1,2,3,4,5,6,7,8)
Even,Odd=0,0
for i in tup:
    if i%2==0:
        EVen+=1
    else:
        Odd+=1
print("Even numbers count:",Even)
print("Odd numbers count:",Odd)


#20.Accept a number from the user and determine whether it exists in the tuple.
print("\n\n20.determine whether it exists in the tuple")
tup=(56,34,2,67,22,89,100)
num=input("Enter number to search:")
for i in tup:
    if i==num:
        print("Exist")
    else:
        print("Not Exist")
        break


"""21.Store student details in a tuple:
Roll Number 
Name 
Department 
Marks"""
print("\n\n21.Store student details in a tuple")
tup=((101,'Shreya','CSE',95),(102,'Dipali','Civil',85),(103,'Sayali','DS',90))
for i in tup:
    print(i)


"""Display all the details.
22.Create tuples containing:
Employee ID 
Name 
Salary
 Display all employee information."""

print("\n\n22.Store Employee details in a tuple")
tup=((101,'Shreya',100000),(102,'Anushka',50000),(103,'Tanvi',60000))
for i in tup:
    print(i)


"""23.Store item prices in a tuple and calculate:
Total bill 
Average price 
Highest-priced item 
Lowest-priced item"""
print("\n\n23.Store item prices in a tuple and calculate")
tup=(100,200,300,400,500)
print("Total bill",sum(tup)) 
print("Average price:",sum(tup)/len(tup))
print("Highest-priced item:",max(tup)) 
print("Lowest-priced item:",min(tup))


"""24.Store temperatures of seven days in a tuple and determine:
Maximum temperature 
Minimum temperature 
Average temperature"""
print("\n\n24.Store temperatures of seven days in a tuple")
tup=(23,25,27,30,31,32,34) 
print("Average temperature:",sum(tup)/len(tup))
print("Maximum temperature:",max(tup)) 
print("Minimum temperature:",min(tup))


"""25.Store runs scored in 10 matches and calculate:
Total runs 
Highest score 
Lowest score 
Average score"""
print("\n\n25.Store runs scored in 10 matches")
tup=(23,25,27,30,31,32,34)
print("Total runs:",sum(tup))
print("Average score:",sum(tup)/len(tup))
print("Highest score:",max(tup)) 
print("Lowest score:",min(tup))


#26.Create two tuples and find the common elements between them.
print("\n\n26.Create two tuples and find the common elements between them.")
t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)
common = tuple(set(t1) & set(t2))
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Common elements:", common)


#27.Merge two tuples and remove duplicate elements.
print("\n\n27.Merge two tuples and remove duplicate elements.")
t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)
merged = tuple(set(t1 + t2))
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Merged tuple without duplicates:", merged)



#28.Count the frequency of each element in a tuple.
print("\n\n28.Count the frequency of each element in a tuple")
t = (10, 20, 10, 30, 20, 10, 40, 30)
frequency = {}
for item in t:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Tuple:", t)
print("Frequency of each element:")
for item, count in frequency.items():
    print(item, ":", count)


#29.Convert a tuple into a sorted tuple in ascending and descending order.
print("\n\n29.Convert a tuple into a sorted tuple in ascending and descending order.")
t = (50, 20, 40, 10, 30)
ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))
print("Original tuple:", t)
print("Ascending order:", ascending)
print("Descending order:", descending)



"""30.Create a tuple containing patient records:
Patient ID 
Name 
Age 
Blood Group """

patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 40, "O+"),
    (104, "Sneha", 28, "A+"),
    (105, "Rohan", 35, "O-")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
search_id = 103
print("\nSearching for Patient ID:", search_id)
found = False
for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)
        found = True
        break

if not found:
    print("Patient not found")

# Count total patients
print("\nTotal number of patients:", len(patients))

# Display patients with specific blood group
blood_group = "A+"

print("\nPatients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
