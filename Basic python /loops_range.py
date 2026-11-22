number  = [1,2,3,4,5,6,7,8,9,10]

for value in number:
    if (value % 2 == 0):
        print(value, "is even")
    else:
        print(value, "is odd")



for _, value in range(len(number)):
    print(value)