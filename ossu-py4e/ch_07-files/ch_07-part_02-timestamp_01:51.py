from itertools import count


fhand = open('ch_01-part-01.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)