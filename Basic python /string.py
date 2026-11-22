
str = 'Amit form pune work in fittr'
str2 = 'Talole'

print ("length of str is: ", len(str))
print ("length of str2 is: ", len(str2))
print(str.strip() + ' ' + str2.strip())

print("endwith",str.endswith('t') == True)
print("lower",str.lower())
print("upper",str.upper())
print("replace", str.replace('Amit','Amit Talole'))

print("count", str.count('Amit'))
print("find", str.find('Amit'))
