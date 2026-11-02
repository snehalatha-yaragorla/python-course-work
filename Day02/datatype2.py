# implicit
num1=100
num2=3.5
c=num1+num2
print(c,type(c))

# explicit
n=int(input())
print(n,type(n))
n2=str(n)
print(n2,type(n2))

str1="Sneha"
print(str1)
lst2=list(str1)
print(lst2,type(lst2))
t2=tuple(lst2)
print(t2,type(t2))
set2=set(lst2)
print(set2,type(set2))

# Read the int,set,list from user
num=int(input())
print(num,type(num))
s=input()
print(s,type(s))
list1=list(map(int,input().split()))
print(list1,type(list1))
tuple1=tuple(map(int,input().split()))
print(tuple1,type(tuple1))
set1=set(map(int,input().split()))
print(set1,type(set1))


