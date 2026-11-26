Functions
# addition of two numbers
def addition(x,y):
    return x+y
print(addition(10,20))

count of vowels and consonents
def alphabet_count(str1):
    vowels_count=0
    consonents_count=0
    for ch in str1:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels_count+=1
            else:
                consonents_count+=1
    return [vowels_count,consonents_count]
print(alphabet_count("python project"))
print(alphabet_count("pavithra"))
print(alphabet_count("sneha"))

# 1.with parameters with return
def add1(x,y):
    return x+y
z=add1(10,20)
print(z)

# 2.with parameters without return values
def add2(x,y):
    print(x+y)
add2(10,30)
z=add2(10,20) # returns none because we didn't use return we are just printing
print(z)   

# 3.without parameters with return values
def add3():
    x=100
    y=200
    return x+y
z=add3()
print(z)

# 4.without parameters without return values
def add4():
    x=int(input("enter x value: "))
    y=int(input("enyter y value:"))
    print(x+y)
add4()

# division
# 1.method
def division(x,y):
    if y!=0:
        return x/y,x//y,x%y
    else:
        print("0 is not divisible,please take another number")
a=division(20,10)
print(a)

# 2.method
def division2(x,y):
    if y!=0:
        print(x/y)
    else:
        print("0 is not divisible,please take another number")
division2(20,10)

# 3 method
def division3():
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    if y!=0:
        return x/y
    else:
      print("0 is not divisible,please take another number")  
z=division3()
print(z)

# 4 method
def division4():
    x=int(input("enter x value: "))
    y=int(input("enter y value: "))
    if y!=0:
        print(x/y)
    else:
        print("0 is not divisible,please take another number")
division4()