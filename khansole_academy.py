"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""
import random
MIN_RANDOM = 10
MAX_RANDOM = 99
NUM_CORRECT = 3


def main():
    score = 0
    while score < 3:
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        correct_answer = num1 + num2
        print("What is " + str(num1) + " + " + str(num2) + "?")
        user_answer = int(input("Your answer is: "))
        if user_answer != correct_answer:
            score = 0
            print("Incorrect. The expected answer is " + str(correct_answer))
        else:
            score += 1
            print("Correct! You've gotten " + str(0+score) + " correct in a row.")
    print("Congratulations!You mastered addition.")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
