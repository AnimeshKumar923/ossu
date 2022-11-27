import numpy
import math

### code for exponent calculation

# input for number x

x = input('enter number x: ')

# print(x)

y=input('enter number y: ')

# print(type(x))
# print(type(y))

y_int=int(y)
x_int=int(x)

# print(type(y_int))
# print(type(x_int))


power=x_int**y_int

print(power)



# code to compute logarithm

print(math.log2(x_int))