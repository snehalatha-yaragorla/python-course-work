d = {}
d1= dict()
d2={'a':1,'b':2,'c':3}
print(type(d))
print(type(d1))
print(type(d2))

print(d2['a']) # access value using key

print(d2.values()) # access all values
print(d2.keys()) # access all keys
print(d2.items()) # access all items

d2['c']=6 #update value using key
print(d2)

d2['d']=4 # add new key-value pair
print(d2)

d2.update({'e':5,}) # update using update() method
print(d2)

d2.update(f=6) # update using updatea() method
print(d2)

print(d2.get('c')) # access value using get() method
# print(d2['z']) # will give error if keyt is not found
print(d2.get('z')) # will return none if key is not found
print(d2.get('z',0)) # will return default value if key is not found

d2.pop('a') # reomve key-value pair using pop() method
print(d2)
#d2.pop('a') # will give error if key is not found
#print(d2)
d2.pop('a',None) # will not give error if key is not found
print(d2)

d2.popitem() # remove last inserted key-value pair
print(d2)

d2.clear() # remove all-key valie pairs
print(d2)

del d2 # delete entire dictionary
#print(d2) # will give error as d2 is deleted
