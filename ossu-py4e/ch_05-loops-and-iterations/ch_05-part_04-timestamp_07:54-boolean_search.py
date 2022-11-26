found = False
print('Before', found)
for value in [34,56,32,4,7,9,98,0]:
    if value == 9:
        found = True
    print(found, value)
print('After', found)