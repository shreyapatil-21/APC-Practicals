    
#1.Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.
import numpy as np
arr1=np.array([23,34,56,78])
print("One dimensional array:",arr1)
print("size of arr1:",arr1.size)
print("Type of array:",arr1.dtype)
print("no of dimensions:",arr1.ndim)
print("*******************************************")
#2.	Create two NumPy arrays of 5 integers each. Perform and display:

#•	Addition 
#•	Subtraction 
#•	Multiplication 
#•	Division 
#•	Modulus
import numpy as np
arr2=np.array([11,12,13,14,15])
arr3=np.array([1,2,3,4,5])
print("Addition is:",np.array(arr2+arr3))
print("Subtraction is:",np.array(arr2-arr3))
print("Multiplication is:",np.array(arr2*arr3))
print("Division is:",np.array(arr2/arr3))
print("Modulus is:",np.array(arr2%arr3))
print("*******************************************")      


#3. Create a NumPy array containing 10 numbers
arr4 = np.array([11, 2, 34, 48, 59, 6, 72, 18, 79, 100])

print("Minimum element is:", min(arr4))
print("Maximum element is:", max(arr4))

total = 0
for i in arr4:
    total = total + i

print("Sum is:", total)

avg = total / arr4.size
print("Average is:", avg)

print("*******************************************")     


#4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
a=np.arange(1,21)
even=a[a%2==0]
odd=a[a%2!=0]
print("even numbers are:",even)
print("Odd numbers are:",odd)
print("*******************************************")      

#5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
#•	2 × 6 matrix 
#•	3 × 4 matrix 
#•	4 × 3 matrix
b=np.arange(1,13)
print("2*6 matrix:",b.reshape(2,6))
print("3*4 matrix:",b.reshape(3,4))
print("4*3 matrix:",b.reshape(4,3))
print("*******************************************")

#6.	Create two 3 × 3 NumPy matrices and perform matrix addition.
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=np.array([[11,12,13],
            [14,15,16],
            [17,18,19]])
c=a+b
print("Addition is:",c)
print("*******************************************")  

#7.	Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
arr5=np.array([[2,4],[3,5]])
arr6=np.array([[22,24],[26,4]])
ans=np.matmul(arr5,arr6)
print("Matrix multiplication is:",ans)
print("*******************************************")

#8.	Create a 3 × 4 matrix and display its transpose.
arr7=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr7.T)
               
#9.	Create a 4 × 4 NumPy array and write a program to:
#•	Display the first row 
#•	Display the last column 
#•	Display the diagonal elements 
#•	Display the elements from the second and third rows
ar=np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]])

print("First row:")
print(ar[0])

print("Last column:")
print(ar[:,-1])

print("Diagonal elements:")
print(np.diag(ar))

print("Second and third rows:")
print(ar[1:3])

print("*******************************************")

#10.	Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Sum of each row:")
print(np.sum(arr, axis=1))

print("Sum of each column:")
print(np.sum(arr, axis=0))
print("*******************************************")

#11.	Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
#•	First 5 elements 
#•	Last 5 elements 
#•	Alternate elements 
#•	Elements in reverse order
import numpy as np

arr = np.arange(1, 21)

print("Array:")
print(arr)

print("First 5 elements:")
print(arr[:5])

print("Last 5 elements:")
print(arr[-5:])

print("Alternate elements:")
print(arr[::2])

print("Elements in reverse order:")
print(arr[::-1])
print("*******************************************")

#12.Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np

arr = np.array([25, 60, 45, 75, 30, 90, 55, 40, 80, 20])

print("Original array:")
print(arr)

arr[arr > 50] = 0

print("Array after replacing elements greater than 50 with 0:")
print(arr)
print("*******************************************")

#13.	Create an unsorted NumPy array and display it in:
#•	Ascending order 
#•	Descending order
import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56])

print("Original array:")
print(arr)

print("Ascending order:")
print(np.sort(arr))

print("Descending order:")
print(np.sort(arr)[::-1])

#14.	Create an array containing duplicate values. Find and display only the unique elements.
import numpy as np

arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 10, 40])

print("Original array:")
print(arr)

print("Unique elements:")
print(np.unique(arr))

#15.	Create two NumPy arrays and concatenate them horizontally and vertically. 
import numpy as np

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print("Horizontal concatenation:")
print(np.hstack((arr1, arr2)))

print("Vertical concatenation:")
print(np.vstack((arr1, arr2)))

#16.	Store marks of 10 students in a NumPy array. Calculate:
#•	Highest marks 
#•	Lowest marks 
#•	Average marks 
#•	Median 
#•	Standard deviation
import numpy as np

marks = np.array([78, 85, 67, 90, 72, 88, 95, 60, 76, 82])

print("Marks:")
print(marks)

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))

#17.	Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
import numpy as np

marks = np.array([65, 78, 82, 55, 90, 72, 68, 88, 76, 95,
                  60, 84, 70, 92, 58, 80, 75, 85, 66, 89])

average = np.mean(marks)

print("Class average:", average)

print("Marks above average:")
print(marks[marks > average])

#18.	Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its:
#•	Number of dimensions 
#•	Shape 
#•	Size
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

#19.	Create a 3D array of shape (2, 3, 4) and write a program to access:
#•	First element 
#•	Last element 
#•	Element at index [0,1,2] 
#•	Element at index [1,2,3]
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("First element:", arr[0, 0, 0])

print("Last element:", arr[1, 2, 3])

print("Element at index [0,1,2]:", arr[0, 1, 2])

print("Element at index [1,2,3]:", arr[1, 2, 3])

#20.	Create a (2, 3, 4) array and calculate:
#•	Sum of all elements 
#•	Sum of each layer 
#•	Sum along rows 
#•	Sum along columns
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)


print("Sum of all elements:", np.sum(arr))


print("Sum of each layer:")
print(np.sum(arr, axis=(1, 2)))


print("Sum along rows:")
print(np.sum(arr, axis=2))


print("Sum along columns:")
print(np.sum(arr, axis=1))

#21.	Create a 3D array of random integers between 1 and 100. Replace all values greater than 50 with 0
import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("Array after replacing values greater than 50 with 0:")
print(arr)

#22.	Generate a random 3D array of shape (3, 4, 5) and calculate its:
#mean, median, standard deviation, variance, minimum, and maximum.
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

#23.	Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.
import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array:")
print(arr)

flat = arr.flatten()

print("Flattened Array:")
print(flat)

#24.	Create a 3D array containing integers from 1 to 27. Flatte3n the array and calculate:
#•	Sum 
#•	Average 
#•	Maximum 
#•	Minimum
import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

flat = arr.flatten()

print("3D Array:")
print(arr)

print("Flattened Array:")
print(flat)

print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))

#25.	Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:
#•	Greater than 50 
#•	Even numbers 
#•	Less than the average value
import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()

print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flat)

print("Elements greater than 50:")
print(flat[flat > 50])

print("Even numbers:")
print(flat[flat % 2 == 0])

average = np.mean(flat)

print("Average:", average)

print("Elements less than average:")
print(flat[flat < average])	

