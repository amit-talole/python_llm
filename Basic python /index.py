

first = input("Enter the first number: ")
second = input("Enter the second number: ")

def basic_function(a: int, b: int) -> int:
    """Raise the first number to the power of the second number"""
    try:
        return a ** b
    except Exception as e:
        print("An error occurred:", e)
        return 0

result = basic_function(int(first), int(second))

print("result: ", result)


