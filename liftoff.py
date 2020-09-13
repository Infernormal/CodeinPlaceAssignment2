"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    NUM_START = 10
    print(str(NUM_START))
    for i in range(9):
        NUM_START -= 1
        print(str(NUM_START))
    print("Liftoff!")


    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
