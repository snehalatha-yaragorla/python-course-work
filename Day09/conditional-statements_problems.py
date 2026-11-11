# user tries to withdraw money from ATM. if withdraw < amount allow it.
# otherwise show insuufficient balance message
amount = int(input("enter your amount to withdraw: "))
bal = 20000
if amount <= bal:
    print("withdraw Successful")
    bal -= amount
    print("remaining balance is: ",bal)
else:
    print("Insufficient Balance")

# ATM can only withdraw amount in multiples of 100, 200, 500.
amount = int(input("enter your amount to withdraw: "))
bal = 20000
if (amount % 100 ==0) or (amount % 200 == 0) or (amount % 500 ==0):
    if amount <= bal:
        print("withdraw Successful")
        bal -= amount
        print("remaining balance is: ",bal)
    else:
        print("Insufficient Balance")
else:
    print("Invalid amount. Please enter correct amount.")

# A Customer shops on an online store. if total amount is 2000 or more, give 20% discount.
# otherwise no discount. show final price message.
amount = float(input("enter your bill amount : "))
if amount >= 2000:
    discount = (20/100) * amount
    final_price = amount - discount
    print("your final price is : ",final_price)
else:
    print("your final price is : ",amount)

# another way to write the above code is 
amount = float(input("enter your bill amount : "))
if amount >= 2000:
    discount = amount * 0.2
    print("discount amount is : ",discount)
    final_price = amount - discount
    print("your final price is : ",final_price)
else:
    print("your final price is : ",amount)

# A System checks password length. if the length is  8 or more password accepted.
# otherwise rejected.Display result
password = input("Enter your pssword: ")
if len(password) >= 8:
    print("password accepted")
else:
    print("password rejected,please select the password more than 8 characters")

# Read time in 24-hour format and convert it to 12-hour foramt with AM/PM
hours = int(input("hors: "))
minutes = int(input("minutes: "))
if hours<=12:
    print("time is :",hours,":",minutes)
else:
    hours = hours % 12
    print("time is: ",hours,":",minutes)

# check whether the number is positive or negative or zero
n = int(input("enter number: "))
if n > 0 and n % 2 == 0:
    print("Positive and even")
elif n > 0 and n % 2 != 0:
    print("positive and odd")
elif n < 0 and n % 2 ==0:
    print("negative and even")
elif n < 0 and n % 2 != 0:
    print("negative an odd")
else:
    print("zero")

# Another Approach
n = int(input("enter number: "))
if n>0:
    if n%2==0:
        print("positive and even")
    else:
        print("positive and odd")
elif n<0:
    if n%2==0:
        print("negative and even")
    else:
        print("negative and odd")
else:
    print("zero")