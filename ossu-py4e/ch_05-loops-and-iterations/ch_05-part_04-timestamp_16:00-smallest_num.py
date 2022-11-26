smallest = None
print('Before')
for value in [10,41,12,5,3,1,45,678,]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# "is" and "is not" are powerful operators that "==" but recommended to use it only in boolean (T/F) and in "None" function.