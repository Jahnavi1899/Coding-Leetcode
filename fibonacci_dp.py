def fibonacci(n, dp_arr):
    if n <= 1:
        return n
    if dp_arr[n] == -1:
        dp_arr[n] = fibonacci(n-1, dp_arr) + fibonacci(n-2, dp_arr)
    return dp_arr[n]

def fib_tabular(n):
    prev1 = 1
    prev2 = 0

    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

    

n = 10
dp_arr = [-1 for _ in range(n+1)]
# print(fibonacci(n, dp_arr))
print(fib_tabular(10))

