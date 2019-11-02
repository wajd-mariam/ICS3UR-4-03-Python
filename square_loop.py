# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program calculates the square of a number


def main():
    # variables
    answer = 0
    counter = 1

    # input
    number = int(input("Enter a number to loop it and square its results: "))

    # process & output
    for counter in range(number + 1):
        answer = counter **2
        print(str(counter) + "² = " + str(answer))


if __name__ == "__main__":
    main()
