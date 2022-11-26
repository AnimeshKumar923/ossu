# tuples are comparable

# the comparison operators work with tuples and other sequences.
# if the first item is equal, python goes on to the next element, and so on, until it finds elements that differ.

a = (0,1,2) < (5,1,2)

b = (0,1,2000) < (0,3,4)

c = ('Jones', 'Sally') < ('Jones', 'Sam')

d = ('Jones', 'Sally') < ('Adams', 'Sam')

print(a)
print(b)
print(c)
print(d)