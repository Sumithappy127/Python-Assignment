def fibonacci_series(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
if n <= 0:
        print("Please enter a positive integer.")
else:
        series = fibonacci_series(n)
        print("The Fibonacci sequence up to", n, "terms is:")
        print(series)

