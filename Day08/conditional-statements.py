# # if Statement
# age=23
# if age>=18:
#     print("you are eligible to vote")

# # if-else Statement
# num=int(input("enter a number: "))
# if num>0:
#     print("positive")
# else:
#     print("Negative")

# # even or odd
# num=int(input("enter a number: "))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# # create a simple ATM withdrawal eligibilty program.
# bal=20000
# amount=int(input("Enter withdraw amount: "))
# if amount>=100 and amount<=bal:
#     print("withdraw Successfull")
# else:
#     print("withdraw not possible")

# if-elif-else statements
marks=90
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=60:
    print("grade C")
elif marks>=35:
    print("grade D")
else:
    print("failed")

# among 3 numbers find greatest number
a,b,c=map(int,input("enter 3 numbers: ").split(" "))
if a>b and a>c:
    print(a,"is large number")
elif b>c:
    print(b,"is large number")
else:
    print(c,"is large number")

# Fizz Buzz
num=6
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("Not divisible")

# nested if statements
# among 3 numbers find greatest number
a,b,c=map(int,input("enter 3 numbers: ").split(" "))
if a>b:
    if a>c:
        print(a,"is large number")
    else:
        print(c,"is large number")
else:
    if b>c:
        print(b,"is large number")
    else:
        print(c,"is large number")