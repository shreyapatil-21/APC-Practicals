#1.Write a Python program to create a set containing five integers and display all its elements.
print("1.Set with 5 elements")
s={1,2,3,4,5}
print(s)


#2.Create a list containing duplicate values. Convert the list into a set and display the resulting set.
print("\n\n2.Convert the list into a set")
ls=[1,2,3,4,5,6,7,2,2,1,5]
s=set(ls)
print(s)


#3.Create a set of five fruits.
#Add two new fruits using appropriate set methods and display the updated set.
print("\n\n3.set of five fruits")
s={'Apple','Banana','Guava','Watermelon','Mango'}
s.add('Kivi')
s.add('Chiku')
print("After Adding:\n",s)


#4.Create a set of numbers and remove a specified number from the set.
print("\n\n4.remove a specified number")
s={1,2,3,4,6,5}
s.remove(6)
print(s)


#5.Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
print("\n\n5.Create a set of student names.")
s={'Shreya','Anushka','Dipali','Sayali','Madhura'}
name=input("Enter name to search:").title()
for i in s:
    if i==name:
        print("Exist")
    else:
        print("Not Exist")
        break


#6.Create a set of cities and determine the total number of cities using an appropriate function.
print("\n\n6.set of cities")
s={'Karad','Satara','Kolhapur','Bawada','Pune'}
print("total number of cities:",len(s))


#7.Create a set of programming languages and display each language using a for loop.
print("\n\n7.set of programming languages")
s={'C','C++','Java','Python','HTML'}
for i in s:
    print(i,end=" ")


#8.Create a list containing duplicate numbers, use a set to remove the duplicates.
print("\n\n8.set to remove the duplicates in list")
ls=[1,2,3,4,5,6,7,2,2,1,5]
s=set(ls)
print("After Removing Duplicates:",s)



#9.Create two sets of integers and find their union.
print("\n\n9.Create two sets of integers and find their union")
s1={1,2,3,4,5}
s2={6,7,8,9,10}
print("Union of sets:",s1.union(s2))


#10.Create two sets and find the elements common to both sets.
print("\n\n10.Create two sets and find the elements common to both sets.")
s1={1,2,3,4,5}
s2={6,2,3,9,10}
print("Intersection of sets:",s1.intersection(s2))


"""11.Create two sets and find:
Elements present in the first set but not the second 
Elements present in the second set but not the first"""
print("\n\n11.Create two sets and find difference")
s1={1,2,3,4,5}
s2={6,2,3,9,10}
print(s1.difference(s2))
print(s2.difference(s1))


#12.Create two sets of numbers and
#find the elements that are present in either set but not in both.
print("\n\n12.Create two sets and find symmetric_difference")
s1={1,2,3,4,5}
s2={6,2,3,9,10}
print(s1.symmetric_difference(s2))



#13.Create two sets and determine whether the first set is a subset of the second set.
print("\n\n13.determine whether the first set is a subset of the second set")
s1={2,3}
s2={1,2,3,4,5}
print("first set is a subset of the second set:",s1.issubset(s2))


#14.Create two sets and determine whether the first set is a superset of the second set.
print("\n\n13.determine whether the first set is a superset of the second set")
s1={2,3}
s2={1,2,3,4,5}
print("first set is a superset of the second set:",s1.issuperset(s2))


#15.Write a program to determine whether two sets have no elements in common.
print("\n\n15.Write a program to determine whether two sets have no elements in common.")
s1={6,7,2,8,9}
s2={1,2,3,4,5}
if not s1.intersection(s2):
    print("Have no common elements")
else:
    print("Have common elements")


#16.Create two sets and check whether they are equal.
print("\n\n16.Create two sets and check whether they are equal.")
s1={1,2,3,4,5}
s2={1,2,3,4,5}
if s1==s2:
    print("equal")
else:
    print("not equal")


#17.Two students have selected different subjects.
#Store their subjects in two sets and determine the subjects studied by both students.
print("\n\n17.program")
s1={'C','C++','Python'}
s2={'Java','html','Python'}
print("subjects studied by both students:",s1.intersection(s2))


#18.Accept a sentence from the user and use a set to display all unique words.
print("\n\n18.display all unique words")
str=input("Enter Sentence:")
word=str.split()
freq={}
s=set()
for i in word:
    freq[i]=freq.get(i,0)+1
for i in freq:
    if freq[i]==1:
        s.add(i)
print(s)


"""19.Create two sets:
Students present in the morning session 
Students present in the afternoon session
Find:
Students present in both sessions 
Students present only in the morning 
Students present only in the afternoon 
Students present in at least one session"""

print("\n\n19.find")
morning={'Shreya','Madhura','Vaishu','Dipali'}
afternoon={'Tanvi','Sayali','Shreya'}
print("Students present in both sessions:",morning.intersection(afternoon))
print("Students present only in the morning:",morning.difference(afternoon))
print("Students only in the afternoon:",afternoon.difference(morning))
print("Students present in at least one session",morning.symmetric_difference(afternoon))


"""20.Create sets representing students enrolled in:
Python 
Java """
python={'Shreya','Madhura','Vaishu','Dipali'}
java={'Tanvi','Sayali','Shreya'}


#21.Find students enrolled in both courses and students enrolled in only one course.
print("\n\n21Find:")
print("students enrolled in both courses:",python.intersection(java))
print("students enrolled in only one course:",python.symmetric_difference(java))


"""22.Create two sets representing technical skills of two employees. Find:
Common skills 
Skills unique to Employee 1 
Skills unique to Employee 2 
All available skills"""
print("\n\n22.find:")
e1={'testing','coding','debugging'}
e2={'debugging','designing'}
print("Skills unique to Employee 1:",e1.difference(e2))
print("Skills unique to Employee 2:",e2.difference(e1))
print("All available skills:",e1.union(e2))


#23.Create a set containing available books and another set containing requested books.
#Determine which requested books are available.
print("\n\n23.Find requested books that are available")
available_books = {"Python", "Java", "C++", "HTML", "SQL"}
requested_books = {"Python", "Java", "CSS", "SQL"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)




"""24.Store visitor IDs from two different days in separate sets. Determine:
Unique visitors across both days 
Returning visitors 
Visitors who came only on the first day 
Visitors who came only on the second day
Create sets representing products belonging to different categories.
Find products that belong to both categories."""

print("\n\n24.Find")
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}
print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)
electronics = {"Laptop", "Mobile", "Tablet", "Headphones"}
accessories = {"Mobile", "Headphones", "Charger", "Mouse"}
print("Products in both categories:", electronics & accessories)



"""25.Represent the friends of two users using sets. Find:
Mutual friends 
Friends unique to User 1 
Friends unique to User 2 
Total unique friends"""
print("\n\n25.Find")
user1 = {"Rahul", "Amit", "Sneha", "Priya", "Neha"}
user2 = {"Sneha", "Priya", "Rohan", "Karan"}
print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))
