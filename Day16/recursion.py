# pass by object reference - immutable data type
def f(x):
    print(id(x))
    x=x+10
    print(id(x))
    print(x)
a=10
print(id(a))
f(a)

# pass by object reference - mutable data type
def f2(x):
    print(id(x))
    x.append(100)
    print(id(x))
a=[10,20,30]
print(id(a))
f2(a)

def z(x):
    x=[10,20,30]
    print(id(x))
y=[10,20,30]
print(id(y))
z(y)

# recursion 
def fact(n):
    # base condition
    if n==1 or n==0:
        return 1
    # recursive function call
    return n*fact(n-1)
z=fact(5)
print(z)

def fact(n):
    return n*fact(n-1) # raise error because we are providing error
z=fact(3)
print(z)

# add n natural numbers using recursion
def add(n):
    if n==1:
        return 1
    return n+add(n-1)
z=add(5)
print(z)
z=add(7)
print(z)
z=add(10)
print(z)

def add(n):
    if n==2:
        return 2
    return n+add(n-2)
z=add(10)
print(z)
z=add(20)
print(z)

def add(n):
    if n%2==0:
        if n==2:
            return 2
        return n+add(n-1)
    else:
        if n==1:
            return 1
        return n+add(n-1)
z=add(10)
print(z)
z=add(9)
print(z)

def add(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    return n+add(n-2)
z=add(10)
print(z) 
z=add(9)
print(z)
    