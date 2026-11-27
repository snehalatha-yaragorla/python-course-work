# list comprehension 
l=[10,2,5,7,-2,45,62]
r=[x for x in l]
print(r)

# get each and every character from a string
name='sneha'
char=[ch for ch in name]
print(char)

# convert each and evry character as upper case
name='sneha'
char=[ch.upper() for ch in name]
print(char)

# conditional statements in list comprehension
# get all even numbers in list
l=[1,2,3,4,5,6]
even=[i for i in l if i%2==0]
print(even)
odd=[i for i in l if i%2==1]
print(odd)

# get all natural numbers by using range()
n=int(input("enter a range: "))
num=[n for n in range(1,n+1)]
print(num)

# get all even positioned elements in a tuple
t=(-2,45,72,11,1,3,38,14,61)
l=[t[i] for i in range(len(t)) if i%2!=0]
print(l)

# get all even indexed elements
t=(-2,45,72,11,1,3,38,14,61)
l=[t[i] for i in range(len(t)) if i%2==0]
print(l)

# if-else in list comprehension
l=[1,2,3,4,5,6,7,8,9,10]
result=['even' if i %2==0 else 'odd' for i in l]
print(result)

result=['even' if i%2==0 else 'odd' for i in range(1,11)]
print(result)

# nested loops in list comprehension
indexes=[(i,j) for i in range(4)  for j in range(4)]
print(indexes)