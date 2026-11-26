# positional arguments
def func(x,y):
    return x,y
# func(1) # it returns posistional argument error 
# func(1,2,3) # it retruns error takes 2 positional arguments but 3 were given
func(1,2)

def func(x,y):
    return x,y
a=int(input())
b=int(input())
func(a,b)

# keyyword arguments
def func2(x,y):
    print(x)
    print(y)
a=int(input())
b=int(input())
func2(x=b,y=a)
print()
func2(x=a,y=b)
print()
func2(y=a,x=b)

# default value
def func3(x,y,z=0,w=0):
    return x+y+z+w
print(func3(10,20,30))
print(func3(10,20)) # it will not raise error because by default we provide 0 to z

# variable length arguments
def func4(*arg):
    summ=0
    for num in arg:
        summ+=num
    return summ
print(func4(10,20,30,45))

def func4(*arg):
    return sum(arg)
z=func4(10,20,50,25,56,85)
print(z)

# variable length keyword argumnets
def func5(**kargs):
    print(type(kargs))
    # return sum(kargs.values())
    summ=0
    for num in kargs.values():
        summ+=num
    print(summ)
print(func5(a=10,b=20,c=30,d=40))