# Leetcode Solutions for factorial, fibonacci, and palindrome problems

# factorial function

def factorial(n):
    result = 1
   
    for i in range(1, n + 1 ):
        print(n)
        result *= i

    return result


print(factorial(5))  # 120


def factorial_recursive(n):
    print("n: ", n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("factorial_recursive:", factorial_recursive(5))  # 120