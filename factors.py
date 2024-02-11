#!/usr/bin/python3

import sys

def factorize(num):
    factors = []
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            factors.append((i, num // i))
    return (factors)

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            factor_pairs = factorize(num)
            for pair in factor_pairs:
                print(f"{num}={pair[0]}*{pair[1]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factor number")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)

