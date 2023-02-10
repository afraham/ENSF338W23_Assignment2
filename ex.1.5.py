import time
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n - 1) + func(n - 2)


def fib_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def timeFibonacci(functions):
    times = []
    for i in range(36):
        start = time.time()
        functions(i)
        end = time.time()
        times.append(end - start)
    return times


timeOriginal = timeFibonacci(func)
timeImproved = timeFibonacci(fib_memo)

plt.plot(range(36), timeOriginal, label="Original Code")
plt.plot(range(36), timeImproved, label="Improved Code")
plt.xlabel("Input (n-value)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
