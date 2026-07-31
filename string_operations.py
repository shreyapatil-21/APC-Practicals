#Write a program to input a string and display its length without using the len() function.
print("1.String Length ")
str=input("Enter a String:")
count=0
for i in str:
    count+=1
print("Length of string is:",count)


#Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
print("\n2.Character Count")
str=input("Enter a String:").lower()
v,c,digit,space,special=0,0,0,0,0
for i in str:
    if i in 'aeiou':
        v+=1
    elif i.isalpha():
        c+=1
    elif i.isdigit():
        digit+=1
    elif i==' ':
        space+=1
    else:
        special+=1
print("Vowels:",v,"\nConsonants:",c,"\nSpaces:",space,"\nDigits:",digit,"\nSpecial:",special)


#3.Reverse a String
print("\nReverse a String ")
str=input("Enter a String:")
res=""
for i in str:
    res=i+res
print("Reverse string is:",res)


#4.Palindrome Check 
print("\nPalindrome Check  ")
str=input("Enter a String:")
res=""
for i in str:
    res=i+res
if str==res:
    print("Palindrome")
else:
    print("Not Palindrome")


#5.Uppercase and Lowercase Count  
print("\nUppercase and Lowercase Count ")
str=input("Enter a String:")
upper,lower=0,0
for i in str:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print("Uppercase:",upper,"\nLowercase:",lower)


#6.Replace all occurrences of a given character with another character.  
print("\nReplace Characters")
str="Hello World"
upper,lower=0,0
print(str.replace('o','m'))

#7.Remove all spaces from the input string. 
print("\nRemove all spaces")
st=input("Enter a String:")
res=""
for ch in st:
    if ch!=' ':
        res=res+ch
print(res)


#8.Frequency of a Character  
print("\n8.Frequency of a Character ")
st=input("Enter a String:")
ch=input("Enter Character to find:")
count=0
for i in st:
    if i==ch:
        count+=1
print(ch,':',count)


#9. First and Last Character
print("\nFirst and Last Character ")
s=input("Enter a string:")
print("First character:",s[0])
print("Last character:",s[-1])

#10.Display each character of a string along with its ASCII value.
print("\n10.ASCII Values ")
s=input("Enter a string:")
for i in s:
    print(i,'=',ord(i))


#11.Count the total number of words in a sentence.  
print("\nCount the total number of words in a sentence. ")
st=input("Enter a String:")
count=0
for i in st:
    if i==' ':
        count+=1
print('Word Count:',count)


#12.Find the longest word in a given sentence. 
print("\nFind the longest word in a given sentence")
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
print("Length:", len(longest_word))


#13.Find the smallest word in a given sentence. 
print("\nFind the smallest word in a given sentence")
sentence = input("Enter a sentence: ")
words = sentence.split()
smallest_word = ""
for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word

print("Longest word:", smallest_word)
print("Length:", len(smallest_word))

#14.Convert the first letter of every word to uppercase.
print("\n title method()")
str = input("Enter a sentence: ")
str(sentence.title())

#15.Print all duplicate characters in a string.
print("\nPrint all duplicate characters in a string.")
str = input("Enter a string: ")
printed = ""
for ch in str:
    if str.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch


#16.Display the frequency of every character in a string.
print("\nDisplay the frequency of every character in a string.")
str = input("Enter a string: ")
printed = ""
count=0
for ch in str:
    if ch not in printed:
        print(ch,'=',str.count(ch))
        printed += ch


#17.Check whether two strings are anagrams. 
print("\nCheck whether two strings are anagrams.")
s1= input("Enter a string1: ")
s2= input("Enter a string2: ")
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


#18.Remove duplicate characters while maintaining the original order. 
print("\nRemove duplicate characters")
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)  


#19.Check whether a given substring exists in the main string.
print("\nSubstring Search ")
main = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in main:
    print("Substring found")
else:
    print("Substring not found")









