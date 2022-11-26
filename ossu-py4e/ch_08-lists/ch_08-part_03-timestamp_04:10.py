# When you don't specify a delimiter, multiple spaces are treated like one space.
# You can specify the delimiter character to use in the splitting.


line = ' a lot              of spaces'
do = line.split()
print(do)

line2 = 'one;two;three'
split1 = line2.split()
print(split1)

split2 = line2.split(';')
print(split2)

print(split2[1])