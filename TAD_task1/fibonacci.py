n = int(input("Enter which fibonacci number you want to find: "))

def fibonacci(n):
    #base case 1
    if n <= 0:
        return 0
    #base case
    elif n == 1:
        return 1
    else:
        #recursive case
        return fibonacci(n-1) + fibonacci(n-2)

print("The", n, "th fibonacci number is", fibonacci(n))