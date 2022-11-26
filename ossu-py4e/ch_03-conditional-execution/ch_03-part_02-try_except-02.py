astr = 'Bob'

try:
    print("hello")
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)

# line 4 works and line 5 blows up, when this happens 
# the lines below the blown-up line is ignored by python
# and the except block is executed