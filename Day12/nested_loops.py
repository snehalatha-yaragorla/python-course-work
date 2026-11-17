# Nested loops
n=1
for i in range(3):
    for j in range(3):
        print(n,end=" ")
        n+=1
    print()

# Square Matrix
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()

# square matrix with user input
r=int(input("enter no.of rows: "))
c=int(input("enter no.of columns: "))
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()

# Traingle Pattern
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

n=1
for i in range(6):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()

# Hallow square
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# diagnonal pattern 
r=5
for i in range(r):
    for j in range(r):
        if i==j or (i+j)==r-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

# 1 2 3 4 
# 1 2 3 4
# 1 2 3 4 
# 1 2 3 4
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

# printing square pattern by using string repitition
for i in range(4):
    print("* "*4)

# 2  4  6  8
# 1  3  5  7
# 10 12 14 16
# 9  11 13 15
n=1
n1=1
for i in range(4):
    for j in range(4):
        if i%2==0:
            print(n*2,end=(" "))
            n+=1
        else:
            print((n1*2)-1,end=(" "))
            n1+=1
    print()