#LIST
friends=["anila","ammar","5","65.9","False"]

print(friends[0])
print(friends[1:4])
#There are loys of function for the list to make things as per your choice
friends.append("duaa")
print(friends)
#it will append the name at the end of string
l1=[1,8,11,7,9]
l1.sort()
print(l1)
#(l1.sort{the function to sort the value})
l1.insert(4,52)
print(l1)

#TUPLE
a=(1,6,7)

print (a)
print (type(a))
#If u want to makeempty tuple
b=()
print (b)
print(type(b))
#if u take one digit then it will type <int> as it thought it is an integer i...but if you want to type a single digit as a tuple thrn u want to takr comma after a digit like 1,
c=(1)
print(c)
print(type(c))
#As,you find this an integer
d=(1,)
print(d)
print(type(d))
# , after a digit (it will cast type as a tuple)
e=("faira","kaira","zebra",2)
print(type(e))
#e=[0]=454  (it will find an error because u dont use functions as list ,not indrxing,not inserting)
no=e.count("faira")
print(no)
s=e.index(2)
print(s)
print(len(e))
#write a program to store seven fruits as a list entered by user
fruits=[]

f1=input("enter a name:")
fruits.append(f1)

f2=input("enter a name:")
fruits.append(f2)

f3=input("enter a name:")
fruits.append(f3)

f4=input("enter a name:")
fruits.append(f4)

f5=input("enter a name:")
fruits.append(f5)

f6=input("enter a name:")
fruits.append(f6)

f7=input("enter a name:")
fruits.append(f7)
print(fruits)
#write a program to accept mark of 6 students and display them in a sorted manner

marks=[]

f1=int(input("enter a marks:"))
marks.append(f1)

f2=int(input("enter a marks:"))
marks.append(f2)

f3=int(input("enter a marks:"))
marks.append(f3)

f4=int(input("enter a marks:"))
marks.append(f4)

f5=int(input("enter a marks:"))
marks.append(f5)

f6=int(input("enter a marks:"))
marks.append(f6)
marks.sort()

print(marks)
#write a program to sum a list of 4 numbers
l=[57,87,65,43]

print(sum(l))
#write a program to count zeros in the following tuple.
a=(7,0,8,0,0,6,0,0,7)

n=a.count(0)
print(n)
