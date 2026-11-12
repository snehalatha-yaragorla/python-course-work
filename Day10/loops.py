# print n natural numbers
n=int(input("enter a number: "))
for i in range(1,n+1):
    print(i)

name="sneha"
for i in range(len(name)):
    print(name[i])

# print even numbers to one list and odd numbers to another list
n=int(input("enter number: "))
l1=[]
l2=[]
for i in range(1,n+1):
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("Even Numbers list: ",l1)
print("Odd Numbers list: ",l2)

# Factorial program
n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial is: ",fact)

for i in range(1,11,2): # printing odd numbers
    print(i)

for i in range(2,11,2):
    print(i)

# While Loop
# print first five numbers
while i<=5:
    print(i,end=',')
    i+=1

# print reverse order
i=5
while i>=1:
    print(i,end=',')
    i-=1
print()
print(i)

# for loop with else
for i in range(10):
    if i==5:
        break
    print(i)
else:
    print("Loop Completed")

# while loop with else
i=1
while i<=10:
    if i==13:
        break
    print(i)
    i+=1
else:
    print("loop completed")

# Continue
for i in range(5):
    if i==3:
        continue
    print(i,end=" ")

# break
for i in range(5):
    if i==3:
        break
    print(i,end=" ")

# pass
for i in range(5):
    if i==3:
        pass
    print(i,end=" ")

# assert 
assert 10%2==0
print("error")