#!/usr/bin/python3

import sys

def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append((i, number // i))
            n //= i
    if n > 1:
        factors.appen((n, 1))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor_pairs = factorize(number)
            for pair in factor_pairs:
                print(f"{number}={pair[0]}*{pair[1]}")


if __name__ == "__main__":
    main()

