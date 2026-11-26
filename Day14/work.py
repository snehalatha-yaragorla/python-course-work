# find all prime numbers from 2 to 100
def prime():
    n=int(input("enter range: "))
    for i in range(2,n+1):
        f=0
        for j in range(1,i+1):
            if i%j==0:
                f=f+1
                if f>2:
                    break
        if f==2:
            print(i,end=" ")
prime()

# get all the square patterns by using functions
def square():
    r=int(input("enter no.of rows: "))
    c=int(input("enter no.of columns: "))
    for i in range(r):
        for j in range(c):
            print("*",end=" ")
        print()
    n=1
    for i in range(r):
        for j in range(c):
            print(n,end=" ")
            n+=1
        print()
    even=2
    odd=1
    for i in range(r):
        for j in range(c):
            if i%2==0:
                print(odd,end=" ")
                odd+=2
            else:
                print(even,end=" ")
                even+=2
        print()
    for i in range(r):
        for j in range(c):
            if i==0 or j==0 or i==r-1 or j==c-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
    for i in range(r+1):
        for j in range(c+1):
            if i==j or i+j==r:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
square()

# get all triangles 
def triangle():
    for i in range(4):
        for j in range(i+1):
            print("*",end=" ")
        print()
    n=1
    for i in range(4):
        for j in range(i+1):
            print(n,end=" ")
            n+=1
        print()

    for i in range(1,5):
        for j in range(1,i+1):
            print(i,end=" ")
        print()    

    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

    for i in range(4,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

    n=1
    for i in range(4,0,-1):
        for j in range(i,0,-1):
            print(n,end=" ")
            n+=1
        print()

    for i in range(4,0,-1):
        for j in range(i,0,-1):
            print(i,end=" ")
        print()

    for i in range(4,0,-1):
            for j in range(i,0,-1):
                print(j,end=" ")
            print()
    for i in range(4):
        for j in range(4-i):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    print("---------------")
    for i in range(4,0,-1):
        for j in range(4-i):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
triangle()

# pyramids
def pyramid():
    for i in range(3):
        for j in range(3-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
    print("---------")
    for i in range(3,0,-1):
        for j in range(3-i):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
        print()
    print("----------")
pyramid()

# rhombus
def rhombus():
    for i in range(3):
        for j in range(3-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()
    for i in range(2,0,-1):
        for j in range(2-i+1):
            print(" ",end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
        print()
    n=1
    for i in range(3):
        for j in range(3-i-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print(n,end=" ")
            n+=1
        print()
    for i in range(2,0,-1):
        for j in range(2-i+1):
            print(" ",end=" ")
        for j in range(2*i-1):
            print(n,end=" ")
            n+=1
        print()
rhombus()

# add all the values in the dictionary & find minimum,maximum,average amomg the values
def dictionary():
    d={"a":200,"b":30,"c":40,"d":10,"e":60,"f":50}
    summ=0
    maxi=d["a"] # float('-inf')
    mini=d["a"] # float('inf')
    count=0
    for i in d:
        count=count+1
        summ+=d[i]
        if d[i]>maxi:
            maxi=d[i]
        if d[i]<mini:
            mini=d[i]
    print("sum of elements is: ",summ)
    avg =summ/len(d.values())
    #avg=summ/count
    print("average of elements is: ",avg)
    print("maximum elemnet is: ",maxi)
    print("minimum elemnet is: ",mini)
dictionary()

# Reverse a string
def revers(str1):
    rev=""
    for i in str1:
        rev=i+rev
    print("reversed string is: ",rev)
revers("sneha")
revers("pavithra")

# find target element in a list
def lst(l):
    element=int(input("enter element to search: "))
    pos=-1
    for i in l:
        if i==element:
            pos=l.index(i)
    if pos>=0:
        print("position of element is",pos)
    else:
        return -1
z=lst([10,20,30,30,40])
print(z)

# find target elment in a list
l=[1,10,5,6,-55,45]
t=-55
for i in range(len(l)):
    if l[i]==t:
        print(i)
        break
else:
    print(-1)
