#1.zero-nonzero
print("check whether number is zero or nonzero!")
num=int(input("Enter a Number:"))
if num==0:
    print("Zero")
else:
    print("Nonzero")


#2.Largest of 2 numbers
print("\ncheck Largest of 2 numbers!")
a,b=map(int,input("Enter 2 numbers:").split())
if a>b:
    print(a,"is Largest")
else:
    print(b,"is largest")


#3.Positive-Negative
print("\ncheck whether number is positive or negative or zero!")
no=int(input("Enter a number:"))
if no>0:
    print("Positive")
elif no<0:
    print("Negative")
else:
    print("Zero")


#4.character is vowel- or consonant
print("\ncheck whether character is vowel- or consonant!")
ch=input("Enter any single character:")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Character is Vowel")
else:
    print("Character is Consonant")


#5.check student performance
print("\ncheck student performance")
marks=int(input("Enter Marks:"))
if marks>=90:
    print("Excellent Performance!")
elif marks>=80:
    print("Very Good performance!")
elif marks>=70:
    print("Good performance!")
elif marks>=60:
    print("average performance!")
else:
    print("poor performance")


#6.Largest of 3 numbers
print("\ncheck Largest of 3 numbers!")
a,b,c=map(int,input("Enter 3 numbers:").split())
if a>b and a>c:
    print(a,"is Largest")
elif b>a and b>c:
    print(b,"is largest")
else:
    print(c,"is largest")


#7.Smallest of 3 numbers
print("\ncheck Smallest of 3 numbers!")
a,b,c=map(int,input("Enter 3 numbers:").split())
if a<b and a<c:
    print(a,"is Smallest")
elif b<a and b<c:
    print(b,"is Smallest")
else:
    print(c,"is Smallest")


#8.Even-Odd
print("\nCheck Number is Even or Odd")
num=int(input("Enter a Number:"))
if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")


#9.Check whether year is leap or not
print("\nCheck whether year is leap or not")
year = int(input("Enter Year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year!")
else:
    print("Not Leap Year!")

    
#10.whether the driver is insured or not

print("\nwhether the driver is insured or not")
Gender=input("Enter Gender [Male/Female/Other]:")
status=input("Enter Married Status [Married/Unmarried]:")
age=int(input("Enter Age:"))
if status=='Married':
    print("driver is insured")
elif status=='Unmarried' and Gender=='Male' and age>30:
    print("driver is insured")
elif status=='Unmarried' and Gender=='Female' and age>25:
    print("driver is insured")
else:
    print("driver is not insured")
















