# List methods
a=[1,2,3,4,5,6,11,11,7,8,9]
aa=[166,43,11,11,7,8,9]

#Program to find the length of a list
len(a)

#Program to add an element to a list
a.append(10)
#or
a.insert(4,11)

#Program to remove an element from a list
a.remove(11)

#Program to sort a list
a.sort()

#Program to reverse a list
a.sort(reverse=True)

#Program to find the maximum element in a list
b=max(a)
b

#Program to find the minimum element in a list
b=min(a)
b

#Program to check if an element exists in a list
if 2 in a:
  pass

#Program to merge two lists
b=a+a

#Program to find the intersection of two lists
list(set(a) & set(aa))

#Program to find the difference of two lists
list(set(a) - set(aa))

#Program to find the union of two lists
b=a+a