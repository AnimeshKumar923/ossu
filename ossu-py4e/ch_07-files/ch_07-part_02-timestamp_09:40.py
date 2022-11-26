fhand = open('lorem.txt')
for line in fhand:
    line = line.rstrip()
    if not 'lectus' in line:
        continue
    print(line)
