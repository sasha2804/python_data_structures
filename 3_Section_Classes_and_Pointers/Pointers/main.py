# num1 = 11
# num2 = num1

# print('num1 address:', id(num1))
# print('num2 address: ', id(num2))

dict1 = {'value': 11}

dict2 = dict1

print(dict2)

dict2['value'] = 22

print('dict1 address:', id(dict1))
print('dict2 address:', id(dict2))

print(dict1)
print(dict2)

print('dict1 address:', id(dict1))
print('dict2 address:', id(dict2))