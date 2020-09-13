"""
File: nimm.py
-------------------------
Add your comments here.
"""

def main():
    player = 1
    total_stones = 20
    print('There are 20 stones left')
    while total_stones > 0:
        user_answer = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        print("")
        while user_answer <= 0 or user_answer > 2:
            user_answer = int(input("Please enter 1 or 2: "))
        if user_answer == 1:
           print("There are " + str(total_stones-1) + " stones left")
           total_stones -= 1
        else:
            print("There are " + str(total_stones-2) + " stones left")
            total_stones -= 2
        if player == 1:
            player = 2
        else:
            player = 1

    print("Game over! Player " +str(player) + " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
