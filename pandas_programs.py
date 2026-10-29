#1.	Create a dictionary containing the following information for 5 students:
#•	Student ID 
#•	Student Name 
#•	Python Marks 
#•	DBMS Marks 
#•	Mathematics Marks 
#Convert the dictionary into a Pandas DataFrame and:
#1.	Display the DataFrame. 
#2.	Calculate total marks for each student. 
#3.	Calculate average marks. 
#4.	Display students who scored more than 75% average.
import pandas as pd

d = {
    "Id": [101, 102, 103, 104, 105],
    "Name": ["Sayali", "Anushka", "Sanika", "Payal", "Punam"],
    "Python": [75, 34, 67, 89, 12],
    "DBMS": [33, 56, 90, 44, 11],
    "Maths": [88, 56, 34, 12, 90]
}

print("Dictionary:", d)

df = pd.DataFrame(d)

print("\nDataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Avg"] = df["Total"] / 3

print("\nWith Total and Average:")
print(df)

print("\nStudents with Avg > 75:")
print(df[df["Avg"] > 75])


        
#2.	Create a dictionary containing:
#Employee ID
#Employee Name
#Department
#Salary
#Experience
#Convert it into a Pandas DataFrame and:
#1.	Display employees with salary greater than ₹50,000. 
#2.	Find the average salary. 
#3.	Find the highest salary. 
#4.	Find the employee with the highest experience.
emp={
     "emp id":[2,3,4],
     "emp name":["Sayali","Shreya","Deepali"],
     "dept":["HR","Testing","Debugging"],
     "salary":[50000,30000,20000],
     "Experience":[2,3,4]}

print("Original employee list:",emp)
df1=pd.DataFrame(emp)
print("Pandas DataFrames:",df1)
print("Employee wit greater than 50,000:")
print(df1[df1["salary"]>50000])

avg_sal=df1["salary"].mean()
print("Average sal:",avg_sal)
highest_sal=df1["salary"].max()
print("Highest slary:",highest_sal)
highest_exp=df1.loc[df1["Experience"].idxmax()]
print("employee with highest experience:")
print(highest_exp)



#3.	Create a dictionary containing:
#Product ID
#Product Name
#Category
#Price
#Quantity
#Convert it into a DataFrame.
#Calculate:
#Total Amount = Price × Quantity
#Then find the product having the highest total sales.
import pandas as pd

dict1 = {
    "Product_id": [201, 202, 203],
    "Product Name": ["Laptop", "Mouse", "Keyboard"],
    "Category": ["Electronics", "Accessories", "Accessories"],
    "Price": [40000, 5000, 10000],
    "Quantity": [2, 1, 4]
}

df2 = pd.DataFrame(dict1)

print("Pandas DataFrame:")
print(df2)


df2["Total_amount"] = df2["Price"] * df2["Quantity"]

print("DataFrame with total amount:")
print(df2)

highest_sales = df2.loc[df2["Total_amount"].idxmax()]

print("Product having highest total sales:")
print(highest_sales)
        
        
#4.	Create a dictionary containing:
#Patient ID
#Patient Name
#Age
#Disease
#Medical Charges
#Convert the dictionary into a DataFrame and:
#1.	Display patients above 60 years. 
#2.	Find the average medical charge. 
#3.	Find the maximum medical charge. 
#4.	Display patients whose medical charges are greater than ₹50,000. 

dict2={
        "Patient_id":[12,13,14],
        "Patient_name":["Harshee","shrau","Saiidu"],
        "Age":[15,16,17],
        "Disease":["TB","Fever","Cough"],
        "Medical_charges":[500,700,200]}
df3=pd.DataFrame(dict2)
print("Patients DataFrames:")
print(df3)
print("Patients above 60 years:")
print(df3[df3["Age"] > 60])
avg_charges=df3["Medical_charges"].mean()
print("avg charge:",avg_charges)
high_charge=df3["Medical_charges"].max()
print("high charges:",high_charge)
print("Patients with highest charge:")
print(df3[df3["Medical_charges"] > 50000])




#5.	Create a dictionary containing:
#Order_ID
#Customer
#Product
#Quantity
#Price
#Discount
#Create a DataFrame and calculate:
#Final Amount = Quantity × Price − Discount
#Then display:
#•	All orders 
#•	Orders above ₹5,000 
#•	Highest-value order 
#•	Average order value
import pandas as pd

dict4 = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Sayali", "Shreya", "Anushka", "Sanika", "Payal"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Quantity": [2, 5, 3, 1, 4],
    "Price": [40000, 1000, 2000, 12000, 5000],
    "Discount": [5000, 500, 1000, 1000, 2000]
}

df4 = pd.DataFrame(dict4)

df4["Final Amount"] = (df4["Quantity"] * df4["Price"]) - df4["Discount"]

print("All Orders:")
print(df4)

print("\nOrders above ₹5,000:")
print(df4[df4["Final Amount"] > 5000])


print("\nHighest-value order:")
print(df4.loc[df4["Final Amount"].idxmax()])


avg_order = df4["Final Amount"].mean()
print("\nAverage order value:", avg_order)

#6.	Create a dictionary containing:
#Student_ID
#Name
#Department
#Total_Classes
#Classes_Attended
#Create a DataFrame and calculate:
#Attendance Percentage = (Classes_Attended / Total_Classes) × 100
#Display students whose attendance is below 75%.
import pandas as pd

dict5 = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Sayali", "Shreya", "Anushka", "Sanika", "Payal"],
    "Department": ["CSE", "CSE", "IT", "CSE", "IT"],
    "Total_Classes": [100, 100, 80, 90, 100],
    "Classes_Attended": [85, 70, 60, 80, 65]
}

df5 = pd.DataFrame(dict5)

print("Student DataFrame:")
print(df5)

df5["Attendance Percentage"] = (
    df5["Classes_Attended"] / df5["Total_Classes"]
) * 100

print("\nDataFrame with Attendance Percentage:")
print(df5)

print("\nStudents whose attendance is below 75%:")
print(df5[df5["Attendance Percentage"] < 75])

#7.	A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
#Write a Python program to:
#1.	Convert the dictionary into a Pandas DataFrame. 
#2.	Add a new column Total_Sales. 
#3.	Calculate the total sales using Price × Quantity. 
#4.	Display products with sales greater than ₹10,000. 
#5.	Find the product with maximum sales. 
#6.	Calculate the average sales.
import pandas as pd

# Create dictionary
dict6 = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [40000, 500, 1500, 12000, 8000],
    "Quantity": [2, 10, 5, 3, 4]
}

df6 = pd.DataFrame(dict6)

print("Product DataFrame:")
print(df6)


df6["Total_Sales"] = df6["Price"] * df6["Quantity"]

print("\nDataFrame with Total Sales:")
print(df6)


print("\nProducts with sales greater than ₹10,000:")
print(df6[df6["Total_Sales"] > 10000])


print("\nProduct with maximum sales:")
print(df6.loc[df6["Total_Sales"].idxmax()])


average_sales = df6["Total_Sales"].mean()
print("\nAverage sales:", average_sales)

#8.	Create a Pandas Series using a dictionary where the student names are keys and their marks are values.
#Perform:
#•	Display the Series. 
#•	Display marks of a particular student. 
#•	Find maximum and minimum marks. 
#•	Calculate the average marks. 
#•	Display students who scored more than 75.
import pandas as pd
student={
    "sayali":90,
    "Shreya":89,
    "Anushka":88,
    "Sanika":45
    }
s=pd.Series(student)
print("Student Mrks:",s)
print("Marks of Anushka:",s["Anushka"])
print("MAximum marks:",s.max())
print("Minimum marks:",s.min())
print("average marks:",s.mean())
print("Student who scored mor than 75:")
print(s[s>75])

#9.	Create a Pandas Series using a dictionary containing employee names and their salaries.
#Perform:
#•	Display the Series. 
#•	Find the highest salary. 
#•	Find the lowest salary. 
#•	Calculate average salary. 
#•	Display employees earning more than ₹50,000.
emp1={
    "saii":50000,
    "Riya":90000,
    "Harshee":60000}
s1=pd.Series(emp1)
print("employee series:",s1)
print("highest salary:",s1.max())
print("Lowest price:",s1.min())
print("avg salary:",s1.mean())
print("Employee more than 50000:")
print(s1[s1>50000])
    
#10.	Create a Pandas Series using a dictionary containing product names and prices.
#Perform:
#•	Display all products and prices. 
#•	Increase every price by 10%. 
#•	Find the most expensive product. 
#•	Find products costing more than ₹1,000.
products={
    "Chips":50,
    "Chocolates":40,
    "Cold drinks":90}
s2=pd.Series(products)
print("Series of products:",s2)
s2 = s2 * 1.10
print("\nPrices increased by 10%:")
print(s2)
print("most expensive product is:")
print(s2.loc[s2.idxmax()])
print("Products costing more than 1000:")
print(s2[s2>1000])

#11.	Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
#Perform:
#•	Find the average age. 
#•	Find the oldest patient. 
#•	Find the youngest patient. 
#•	Display patients above 60 years.
import pandas as pd

patient = {
    101: 25,
    102: 65,
    103: 45,
    104: 72,
    105: 55
}

s3 = pd.Series(patient)

print("Patient Series:")
print(s3)

print("Average age:", s3.mean())

print("Oldest patient:", s3.max())

print("Youngest patient:", s3.min())

print("Patients above 60 years:")
print(s3[s3 > 60])

#12.	Create a Pandas Series using a dictionary containing student names and attendance percentages.
#Perform:
#•	Find the average attendance. 
#•	Display students with attendance below 75%. 
#•	Display students with attendance above 90%. 
#•	Find the highest attendance.
import pandas as pd

attendance = {
    "Sayali": 85,
    "Riya": 72,
    "Harshee": 95,
    "Anushka": 68,
    "Sanika": 91
}

s4 = pd.Series(attendance)

print("Student Attendance Series:")
print(s4)

print("Average attendance:", s4.mean())

print("Students with attendance below 75%:")
print(s4[s4 < 75])

print("Students with attendance above 90%:")
print(s4[s4 > 90])

print("Highest attendance:", s4.max())

#13.	Dataset: students.csv
#Columns:
#Student_ID,Name,Department,Python,DBMS,Maths
#Problem Statement:
#Read students.csv using Pandas and perform the following:
#1.	Display the first 5 records. 
#2.	Display the last 5 records. 
#3.	Find the total and average marks of each student. 
#4.	Display students whose average marks are greater than 75. 
#5.	Find the student with the highest average. 
#6.	Find the average marks for each subject.
import pandas as pd

df = pd.read_csv(r"C:\Users\BHARAT IT\Desktop\Python\student.csv")

# 1. Display first 5 records
print("First 5 records:")
print(df.head())

# 2. Display last 5 records
print("\nLast 5 records:")
print(df.tail())

# 3. Find total and average marks of each student
df["Total Marks"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average Marks"] = df["Total Marks"] / 3

print("\nTotal and Average Marks:")
print(df[["Student_ID", "Name", "Total Marks", "Average Marks"]])

# 4. Students whose average marks are greater than 75
print("\nStudents with average marks greater than 75:")
print(df[df["Average Marks"] > 75])

# 5. Student with the highest average
print("\nStudent with highest average:")
print(df.loc[df["Average Marks"].idxmax()])

# 6. Average marks for each subject
print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())

#14.	Dataset: employees.csv
#columns:
#Employee_ID,Name,Department,Experience,Salary
#Problem Statement:
#Read the CSV file and:
#1.	Display employees from the CSE department. 
#2.	Find the average salary. 
#3.	Find the highest and lowest salary. 
#4.	Display employees having salary greater than ₹50,000. 
#5.	Calculate department-wise average salary.
import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees with salary > 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
#15.	Dataset: patients.csv
#Columns:
#Patient_ID,Name,Age,Gender,Disease,Medical_Expense
#Problem Statement:
#Read the CSV file and:
#1.	Display patients above 60 years. 
#2.	Calculate average medical expense. 
#3.	Find the patient with the highest medical expense. 
#4.	Count patients for each disease. 
#5.	Display patients whose medical expense exceeds ₹50,000.
import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with highest medical expense:")
print(df[df["Medical_Expense"] == df["Medical_Expense"].max()])

print("\nCount of patients for each disease:")
print(df["Disease"].value_counts())

print("\nPatients with expense > 50000:")
print(df[df["Medical_Expense"] > 50000])
#16.	Dataset: weather.csv
#Columns:
#Date,City,Temperature,Humidity,Rainfall
#Problem Statement:
#Read the CSV file and:
#1.	Find the maximum temperature. 
#2.	Find the minimum temperature. 
#3.	Calculate the average temperature. 
#4.	Display records where temperature is above 35°C.
#5.	Calculate city-wise average temperature.

import pandas as pd

df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords with temperature > 35:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
