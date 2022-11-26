fhand = open('mbox-short.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1


ls = list()

for (key, val) in counts.items():
    newtup = (val, key)
    ls.append(newtup)

ls = sorted(ls, reverse=True)

for (val, key) in ls[:10]:
    print(key, val)
