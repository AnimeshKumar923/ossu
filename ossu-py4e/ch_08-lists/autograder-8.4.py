filename = input('Enter file name: ')

if len(filename) < 1:
    filename = 'mbox-short.txt'

file = open(filename)
count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    
    elif line.startswith('From:'):
        continue
    
    count = count + 1
    words = line.split()
    print(words[1])

print('There were', count, 'lines in the file with From as the first word')