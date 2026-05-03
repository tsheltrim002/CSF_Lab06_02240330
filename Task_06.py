
def iterative_fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq


call_count = 0
def recursive_fibonacci(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

num = int(input("Enter number of terms: "))
print("Iterative Fibonacci:", iterative_fibonacci(num))

call_count = 0
fib_seq = [recursive_fibonacci(i) for i in range(num)]
print("Recursive Fibonacci:", fib_seq)
print("Recursive calls made:", call_count)
