# Fibonacci Number Generator

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

## Mathematical Definition

F(n) = F(n-1) + F(n-2)

where:
- F(0) = 0
- F(1) = 1

## Implementation Examples

### Python Implementation

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage:
print(fibonacci(10))  # Output: 55
```

### Recursive Implementation

```python
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
print(fibonacci_recursive(10))  # Output: 55
```

## Time Complexity Analysis

- Iterative implementation: O(n)
- Recursive implementation: O(2^n)

## Usage Instructions

1. Choose your preferred implementation (iterative or recursive)
2. Call the function with the desired position in the sequence
3. The function will return the Fibonacci number at that position

## Example Output

| Position (n) | Fibonacci Number |
|--------------|------------------|
| 0            | 0                |
| 1            | 1                |
| 2            | 1                |
| 3            | 2                |
| 4            | 3                |
| 5            | 5                |
| 6            | 8                |
| 7            | 13               |
| 8            | 21               |
| 9            | 34               |
| 10           | 55               |

## Notes

- We have used an interative approach which is has better btime complexity
- The recursive implementation is simpler but has exponential time complexity
- For very large numbers, you might want to use memoization or dynamic programming to optimize the recursive solution
