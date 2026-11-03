# Arithmetic Operators
x=10
y=20
print(x+y,x-y,x*y,x/y,x//y,x%y,x**y)

# Assignmant Operators
x=200
print(x)
x+=100
print(x)
x-=200
print(x)
x*=4
print(x)
x//=2
print(x)
x**=2
print(x)
x%=2
print(x)

# Camparision Operators
x=26
y=10
print(x==y,x!=y,x>y,x<y,x>=y,x<=y)

# Logical Operators
x=10
y=20
print((x>y) and (x==y))
print((x<y) or (x!=y))
print(not(x<y))

# Bitwise Operators
n1=45
n2=4
print(n1&n2)
print(n1|n2)
print(n1^n2)
print(~n2)
print(n1>>2)
print(n1<<2)

# Membership Operators
l=[1,2,3,4,5,6]
print(10 not in l)
print(4 in l)
print(5 not in l)

# Identity Operations
x=5
y=5
print(x is y)
a=[1,2,3]
b=a
#b=[1,2,3]
print(a is b)