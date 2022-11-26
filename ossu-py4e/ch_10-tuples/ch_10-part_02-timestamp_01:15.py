# sorting lists of tuples

# we can take advantage of the ability to sort a list of tuples to get sorted version of a dictionary.

# first we sort the dictionary ny the key using the items() method and sorted() function.

d = {'a': 10, 'b': 1, 'c': 22}

items = d.items()

sort = sorted(d.items())

print(items)
print(sort)
