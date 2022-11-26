astr = 'Hello there!'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

#except block is only triggered when the try block blows-up
#try-except is like an insurance policy
#if try block runs then the except block is ignored