# Factors program
n=int(input("enter a number: "))
print("factors of ",n,"is",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()

# find odd numbers in a range
n=int(input("enter a number: "))
print("odd numbers are ",end=" ")
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
print()

# find count of odd numbers in a range
n=int(input("enter a number: "))
c=0
for i in range(1,n+1):
    if i%2!=0:
        c=c+1
print(c)

# prime number
n=int(input("enter a number: "))
f=0
for i in range(1,n+1):
    if n%i==0:
        f=f+1
        if f>2:
            break
if f==2:
    print(n,"is prime number")
else:
    print(n,"is not prime number")

# print prime numbes in a range
n=int(input("enter a number: "))
f=0
for n1 in range(2,n+1):
    f=0
    for i in range(1,n1+1):
        if n1%i==0:
            f=f+1
            # if f>2:
            #     break
    if f==2:
        print(n1,end=" ")
print()

# find perfect number
n=int(input("enter a number: "))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")

# find minimum number from the list
l=[10,26,2,4,45,-3]
mini=l[0]
for i in l:
    if i<mini:
        mini=i
print("minimum element is: ",mini)

# find maximum number from list
l=[10,26,2,4,45,-3]
maxi=l[0]
for i in l:
    if i>maxi:
        maxi=i
print("maximum element is: ",maxi)

# sum of list
l=[10,20,30,40]
summ=0
for i in l:
    summ=summ+i
print("sum of elements is: ",summ)

# length of list
l=[10,20,30,40,50]
length=0
for i in l:
    length+=1
print("legth Of list: ",length)