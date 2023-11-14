def fibonacci(n):
    fib_sequence = [0, 1]  # Die ersten beiden Fibonacci-Zahlen

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Die Liste der Fibonacci-Zahlen in einen kommaseparierten String umwandeln
    fib_str = ', '.join(map(str, fib_sequence[:n]))

    return fib_str
