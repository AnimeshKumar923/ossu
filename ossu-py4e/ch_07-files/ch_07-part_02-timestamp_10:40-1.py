fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('line'):
        count = count+1
print('There were', count, 'lines in', fname)