#!/usr/bin/python3

import sys

def factorize(number):
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return (factors)

def main(filename):
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor_pairs = factorize(number)
            for pair in factor_pairs:
                print(f"{number}={pair[0]}*{pair[1]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factor <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)

