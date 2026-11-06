l=[10,20,30,40]
l.append(50) # adding element
print(l)
print(type(l))
l.append([60,70]) # adding multiple elements in a list
print(l)
l.extend([80,90]) # adding multiple elents in a list by using extend
print(l)
l.insert(2,25) # adding element at specufuc position
print(l)
l.remove(25) # removing element
print(l)
element = 25
if element in l:
    l.remove(element) # removing element which is not in the list
print("no element found")
l.pop() # removing last element
print(l)
l.pop(2) # removing elemnet at specific position
print(l)
l.clear() # removing all elements from the list
print(l)
del l # deleting the list 
print(l) # this will give error because list is deleted
