#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # No numbers to show
    elif length == 1:
        print([0])  # Only the first number
    elif length == 2:
        print([0, 1])  # First two numbers
    else:
        fib = [0, 1]
        for i in range(2, length):
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)
        print(fib)