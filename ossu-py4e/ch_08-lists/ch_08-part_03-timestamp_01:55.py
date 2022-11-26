# Split breaks a string into parts and produces a list of strings.
# We think of these as words. We can access a particular word or loop through all the words.

string = 'Split breaks string'

splitting = string.split()
print(splitting)

print(len(splitting))

print(splitting[1])

print('The words are:')
for w in splitting:
    print(w)