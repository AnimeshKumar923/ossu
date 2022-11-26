# List--> a linear collection of values that stay in order.

# Dictionary--> a "bag" of values, each with its own label.

bag = dict()

bag['money'] = 45
bag['toffee'] = 12
bag['bookmark'] = 23

print(bag)

print(bag['toffee'])

# modifing the value in dictionary 

bag['money'] = bag['money'] + 100
print(bag)

# dictionaries are like lists except that they use keys instead of numbers to look up values.