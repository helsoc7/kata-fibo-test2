def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(sum(fib_sequence[-2:]))

    return fib_sequence[:n]
