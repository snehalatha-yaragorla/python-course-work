# 1 3 5 7
# 2 4 6 8
# 9 11 13 15
# 10 12 14 16
even=2
odd=1
for i in range(1,5):
    for j in range(1,5):
        if i%2==0:
            print(odd,end=" ")
            odd+=2
        else:
            print(even,end=" ")
            even+=2
    print()

# *
# **
# ***
# ****
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# another approach
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# * * * *
#   * * *
#     * *
#       *
for i in range(5,1,-1):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    print()

# another approach
n=4
for i in range(4):
    for j in range(4):
        if i+j>=n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
n=1
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()

# 1
# 2 2 
# 3 3 3
# 4 4 4 4
for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# * * * *
# * * * 
# * * 
# * 
n=4
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# another approach
n=4
for i in range(n):
    for j in range(n):
        if i+j <= n-1:
            print("*",end=" ")
    print()

#   *   
#  * *
# * * *
n=int(input("enter number: "))
for i in range(n):
    # spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    # stars
    for j in range(2*i+1):
        print("*",end=" ")
    print()

# * * *
#  * *
#   *
n=int(input("enter number: "))
for i in range(n):
    # spaces
    for j in range(i):
        print(" ",end=" ")
    # stars
    for j in range(2*n-(2*i+1)):
        print("*",end=" ")
    print()

n=int(input("enter number: "))
for i in range(n):
    # spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    # stars
    for j in range(2*i+1):
        print("*",end=" ")
    print()
n=n-1
for i in range(n):
    # spaces
    for j in range(i+1):
        print(" ",end=" ")
    # stars
    for j in range((2*n)-(2*i+1)):
        print("*",end=" ")
    print()