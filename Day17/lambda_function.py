def add(a,b):
    return a+b
z=add(10,30)
print(z)

# lambda functions
add1=lambda x,y:x+y
print(add1(10,30))

# filter()
nums=[1,2,3,4,5,6,7,8]
even=filter(lambda x:x%2==0,nums)
# print(even)
print(list(even))
# print(tuple(even))

# map()
nums=[1,2,3,4,5,6,7,8]
multiplication_by_2=map(lambda x:x*2,nums)
print(list(multiplication_by_2))

# reduce()
from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,10]
add=reduce(lambda x,y:x+y,nums)
print(add)

nums=[1,2,3,4,5]
even_odd=map(lambda x:'even' if x%2==0 else 'odd',nums)
print(list(even_odd))