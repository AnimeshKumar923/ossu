fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('The file,', fname, ",cannot be opened.")
    quit()

# special function quit() which terminates the code at that point with no further traceback.

count = 0
for line in fhand:
    if line.startswith('Donec'):
        count = count+1
print('There were', count, 'Donec lines in', fname)