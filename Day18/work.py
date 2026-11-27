# genetare squares of sequence from 1 to 10
squares=[i**2 for i in range(1,11)]
print(squares)

# find the length of each string in a list
string=['python','program','method','function']
length=[len(i) for i in string]
print(length)

# extract numbers divisible by 3 and 5
l=[10,20,30,40,50,60]
numbers=[i for i in l if i%3==0 and i%5==0]
print(numbers)

# generate all numbers between 1 to 100 divisible by 7
num=[i for i in range(1,101) if i%7==0]
print(num)

# Extract all words having more than 5 characters
string=['python','program','is','easy','method','function']
length=[i for i in string if len(i)>5]
print(length)

# get all vowels from given string
s='comprehension'
vowels=[i for i in s if i in 'aeiouAEIOU']
print(vowels)

# find all prime numbers from 1 to 100
prime=[i for i in range(2,101) if len([j for j in range(1,i+1) if i%j==0]) == 2]
print(prime)