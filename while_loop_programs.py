print("\n\nLooping Programs")
#1.program to print the natural numbers upto n
print("\n1.program to print the natural numbers upto n")
n=int(input("Enter Value of n:"))
i=1
while(i<=n):
    print(i,end=" ")
    i+=1


#2.program to print even and odd numbers upto n
print("\n2.program to print even and odd numbers upto n")
n=int(input("Enter Value of n:"))
i=1
while(i<=n):
    if i%2==0:
        print(i,"is Even")
    else:
        print(i,"is Odd")
    i+=1

         
#3.program to print sum of natural numbers upto n
print("\n3.program to print sum of natural numbers upto n")
n=int(input("Enter Value of n:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print("sum of natural numbers:",sum)


#4.program to print sum of odd numbers upto n
print("\n4.program to print sum of odd numbers upto n")
n=int(input("Enter Value of n:"))
i=1
sum=0
while(i<=n):
    if i%2==1:
        sum+=i
    i+=1
print("sum of odd numbers:",sum)


#5.program to print sum of even numbers upto n
print("\n5.program to print sum of Even numbers upto n")
n=int(input("Enter Value of n:"))
i=1
sum=0
while(i<=n):
    if i%2==0:
        sum+=i
    i+=1
print("sum of Even numbers:",sum)


#6.program to print natural numbers upto n in reverse order
print("\n6.program to print the natural numbers upto n in reverse order")
n=int(input("Enter Value of n:"))
i=n
while(i>=1):
    print(i,end=" ")
    i-=1

    
#7.program to print fibonacci series upto n
print("\n7.program to print fibonacci series upto n")
n=int(input("Enter Value of n:"))
n1,n2=0,1
i=2
print("Fibonacci Series:\n",n1,"\n",n2)
while(i<=n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i+=1

    
#8.program to check entered number is prime or not
print("\n8.program to check entered number is prime or not")
n = int(input("Enter a number: "))
i = 2
while i < n:
    if n % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")

#9.program to find sum of digits of entered number
print("\n9.program to to find sum of digits of entered number")
n=int(input("Enter Number:"))
sum=0
while(num>0): #123
    n=num%10   #3
    sum+=n
    num//=10
print(sum)

    
#10.program to check entered number is palindrome or not
print("\n10.program to to find sum of digits of entered number")
num=int(input("Enter Number:"))
original=num
rev=0
while(num>0): 
    n=num%10   
    rev=rev*10+n
    num//=10
if rev==original:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")


#11.program to print Multiplication table
print("\n10.program to to find sum of digits of entered number")
num=int(input("Enter Number:"))
i=1
while(i<=10):
    print(i*num,end=" ")
    i+=1


#12.program to print largest and smallest number from n numbers
print("12. Program to print largest and smallest number from n numbers")
n = int(input("Enter how many numbers: "))
num = int(input("Enter number: "))
largest = smallest = num

i = 1
while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    i += 1

print("Largest =", largest)
print("Smallest =", smallest)















