'''s={1,2,3,5}
s1=set()
s2={}
print(type(s))
print(type(s1))
print(type(s2))

s.add(10) # add(element)
print(s) 

s.update({4,6,7}) #update(iterable)
print(s)

s.remove(2) # remove(element)
print(s)

#s.remove(2) 
#print(s) # will give error

s.discard(2) # discard(element)
print(s) # will not give error'''

# set operations
s1={10,20,30,40}
s2={40,50,60}
print(s1)
print(s2)

print("union : ",s1.union(s2)) # union
#print(s1|s2) # union

print("intersection : ",s1.intersection(s2)) # intersection
#print(s1&s2) # intersection

print("difference : ",s1.difference(s2)) # difference
#print(s1-s2) # difference

print("symmetric difference : ",s1.symmetric_difference(s2)) # symmetric difference
#print(s1^s2) # symmetric difference

s3={26,45,18,1,4}
s4={26}
print(s3.issuperset(s4)) # issuperset
print(s3.issubset(s4)) # issubset
print(s4.issubset(s3)) # issubset