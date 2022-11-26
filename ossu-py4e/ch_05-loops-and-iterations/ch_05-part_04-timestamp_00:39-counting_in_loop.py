from itertools import count


count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 45, 232]:
    count = count + 1
    print(count, thing)
print('After', count)