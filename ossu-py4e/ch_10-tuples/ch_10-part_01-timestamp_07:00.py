# tuples and dictionaries

# the items() method in dictionaries returns a list of (key, value) tuples.

d = dict()

d['two'] = 2
d['four'] = 4

for (k,v) in d.items():
    print(k,v)



tups = d.items()
print(tups)