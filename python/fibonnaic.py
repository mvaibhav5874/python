def fibonacci_recursive(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1]+fib_series[-2]
        fib_series.append(next_term)
    return fib_series
n_term = 10
fibonacci_series = fibonacci_recursive(n_term)
print(f"The fibonacci series of {n_term} is")
print(fibonacci_series)
