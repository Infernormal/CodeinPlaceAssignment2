"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    count = 0
    n = int(input("Enter a positive number: "))
    while n != 1:
        if n % 2 == 0:
            y = n/2
            count += 1
            print(str(int(n)) + " is even, so I take half: " + (str(int(y))))
            n = y
        else:
            y = n*3+1
            count += 1
            print(str(int(n)) + " is odd, so I make 3n + 1: " + (str(int(y))))
            n = y
    print("The process took " + str(count) + " steps to reach 1 ")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
