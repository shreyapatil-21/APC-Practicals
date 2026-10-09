n=5
ls=[]
for i in range(0,n):
    marks=int(input("Enter marks:"))
    ls.append(marks)
print("Maximum Marks:",max(ls))
print("Minimum Marks:",min(ls))
print("Average Marks:",sum(ls)/n)
count=0
for i in ls:
    if i>(sum(ls)/n):
        count+=1
print("Students above Average marks:",count)
