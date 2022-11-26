fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Donec'):
        count = count+1
print('There were', count, 'Donec lines in', fname)