fhand = open('line-testing.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('line'):
        print(line)