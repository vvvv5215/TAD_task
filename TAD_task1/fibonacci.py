def fibonacci(n):
    if n <= 0:
        return 0 #base case 1
    elif n == 1:
        return 1 #base case 2
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter which fibonacci number you want to find: "))
print(fibonacci(n))