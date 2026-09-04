# 1. Create student.txt and write student details

with open("student.txt", "w") as f:
    f.write("Name: Shreya Patil\n")
    f.write("Roll Number: 101\n")
    f.write("Branch: Computer Engineering\n")
    f.write("Semester: 4")

print("Student details written successfully")


# 2. Display complete contents of a text file

with open("student.txt", "r") as f:
    data = f.read()

print("\nFile Contents:")
print(data)


# 3. Append additional student information

with open("student.txt", "a") as f:
    f.write("\nCollege: ABC College")
    f.write("\nCity: Kolhapur")

print("\nData appended successfully")


# 4. Read file line by line

print("\nFile line by line:")

with open("student.txt", "r") as f:
    for line in f:
        print(line, end="")


# 5. Count total number of lines

with open("student.txt", "r") as f:
    lines = f.readlines()

print("\n\nTotal number of lines:", len(lines))


# 6. Count total number of words

with open("student.txt", "r") as f:
    data = f.read()

words = data.split()

print("Total number of words:", len(words))


# 7. Count total number of characters including spaces

with open("student.txt", "r") as f:
    data = f.read()

print("Total number of characters:", len(data))


# 8. Display lines in reverse order

with open("student.txt", "r") as f:
    lines = f.readlines()

print("\nLines in reverse order:")

for line in reversed(lines):
    print(line, end="")


# 9. Count vowels and consonants

with open("student.txt", "r") as f:
    data = f.read()

vowels = 0
consonants = 0

for ch in data.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("\nNumber of vowels:", vowels)
print("Number of consonants:", consonants)


# 10. Count alphabets, digits, spaces and special characters

with open("student.txt", "r") as f:
    data = f.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("\nAlphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# 11. Find longest word

with open("student.txt", "r") as f:
    data = f.read()

words = data.split()

longest = max(words, key=len)

print("\nLongest word:", longest)
print("Length:", len(longest))


# 12. Count how many times each word occurs

with open("student.txt", "r") as f:
    data = f.read().lower()

words = data.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord occurrences:")

for word, count in word_count.items():
    print(word, ":", count)


# 13. Search word and display occurrences and line numbers

search_word = input("\nEnter word to search: ")

count = 0

with open("student.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        words = line.split()

        for word in words:
            if word.lower() == search_word.lower():
                count += 1
                print("Found at line:", line_number)

print("Total occurrences:", count)


# 14. Replace a word with another word

old_word = input("\nEnter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as f:
    data = f.read()

data = data.replace(old_word, new_word)

with open("student.txt", "w") as f:
    f.write(data)

print("Word replaced successfully")


# 15. Remove single-line comments from Python source file

with open("program.py", "r") as f:
    lines = f.readlines()

with open("without_comments.py", "w") as f:
    for line in lines:
        if not line.strip().startswith("#"):
            f.write(line)

print("\nComments removed successfully")


# 16. Create another file with uppercase text

with open("student.txt", "r") as f:
    data = f.read()

with open("uppercase.txt", "w") as f:
    f.write(data.upper())

print("Uppercase file created successfully")


# 17. Student records

with open("students.txt", "r") as f:
    lines = f.readlines()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append((int(roll), name, int(marks)))

print("\nAll Student Records:")

for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest)

total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage marks:", average)

print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student)


# 18. Employee records

def read_employees():
    employees = []

    with open("employees.txt", "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append(
                (int(emp_id), name, dept, float(salary))
            )

    return employees


def display_employees(employees):
    print("\nAll Employees:")

    for emp in employees:
        print(emp)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("\nHighest Paid Employee:")
    print(employee)


def average_salary(employees):
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)
    print("\nAverage Salary:", average)


def above_salary(employees, amount):
    print("\nEmployees earning above", amount)

    for emp in employees:
        if emp[3] > amount:
            print(emp)


employees = read_employees()

display_employees(employees)
highest_paid(employees)
average_salary(employees)

amount = float(input("\nEnter salary: "))
above_salary(employees, amount)


# 19. Student attendance

with open("attendance.txt", "r") as f:
    lines = f.readlines()

print("\nStudents having attendance below 75%:")

for line in lines:
    roll, name, present, total = line.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    if percentage < 75:
        print(name, "-", percentage, "%")


# 20. Deposits and withdrawals

total_deposit = 0
total_withdrawal = 0
largest_transaction = 0

with open("transactions.txt", "r") as f:
    for line in f:
        transaction, amount = line.strip().split(",")

        amount = float(amount)

        if transaction == "D":
            total_deposit += amount
        elif transaction == "W":
            total_withdrawal += amount

        if amount > largest_transaction:
            largest_transaction = amount

final_balance = total_deposit - total_withdrawal

print("\nTotal Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)


# 21. Book Management System

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")

    print("Book added successfully")


def search_book():
    book_id = input("Enter Book ID to search: ")

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("Book Found:", data)
                return

    print("Book not found")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    with open("books.txt", "r") as f:
        lines = f.readlines()

    found = False

    for i in range(len(lines)):
        data = lines[i].strip().split(",")

        if data[0] == book_id:
            found = True

            if data[3] == "Available":
                data[3] = "Issued"
                lines[i] = ",".join(data) + "\n"
                print("Book issued successfully")
            else:
                print("Book is already issued")

    with open("books.txt", "w") as f:
        f.writelines(lines)

    if not found:
        print("Book not found")


def return_book():
    book_id = input("Enter Book ID to return: ")

    with open("books.txt", "r") as f:
        lines = f.readlines()

    found = False

    for i in range(len(lines)):
        data = lines[i].strip().split(",")

        if data[0] == book_id:
            found = True
            data[3] = "Available"
            lines[i] = ",".join(data) + "\n"
            print("Book returned successfully")

    with open("books.txt", "w") as f:
        f.writelines(lines)

    if not found:
        print("Book not found")


def display_available():
    print("\nAvailable Books:")

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[3] == "Available":
                print(data)


while True:
    print("\n--- BOOK MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        print("Program ended")
        break
    else:
        print("Invalid choice")


# 22. Combine two text files into a third file

with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("file3.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

print("\nTwo files combined successfully")


# 23. Compare two text files

with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()

with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("\nBoth files are identical")
else:
    print("\nFiles are different")

    min_lines = min(len(lines1), len(lines2))
    found = False

    for i in range(min_lines):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            found = True
            break

    if not found:
        print("One file has additional lines.")


# tell() and seek() method

with open("student.txt", "r") as f:
    print("\nInitial position:", f.tell())

    data = f.read(5)
    print("Read data:", data)

    print("Position after reading:", f.tell())

    f.seek(0)
    print("Position after seek(0):", f.tell())

    data = f.read(10)
    print("Data after seek:", data)
