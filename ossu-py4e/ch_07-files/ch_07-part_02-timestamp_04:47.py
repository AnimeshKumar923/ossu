fhand = open('line-testing.txt')
for line in fhand:
    if line.startswith('line'):
        print(line)