# Paripon Thanthong
# Date : 02/05/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/LysRaG_4fjY

# People Pyramid
# Recursive problem.

# Note : True = 1 , False = 0
def intro():
    print("""Welcome to the Happy Pyramid Program.
    Instruction :

    The Program will ask you to enter 2 numbers refer to the position of the person in the pyramid that
    you want to know how the total weight is on their shoulder.

    Note: Everyone in the pyramid will be assumed that they have 128 pounds.
    """)


def input_user():
    """Function that take 2 numbers indicate the position of the person the user want to know the weight. """
    while True:
        try:
            input_row = int(input('Enter the First position number :'))
            input_column = int(input('Enter the Second position number :'))
            if input_row < 0 > input_column or input_column > input_row:
                print('This location is not exist ! Try other pair that column in less than equal to row.')
            else:
                return input_row,input_column
        except ValueError:
            print('This is not an expected value.')


def humanPyramid(row,column):
    """Human Pyramid function
    That output the weight of the person in particular position in form of matrix (row,column)"""
    if row < 0 > column or column > row:   # This is for out of range position. And, unrealistic position.
                                           # It is impossible that number of column will be over number of row.
        return False
    return 128+(humanPyramid(row - 1, column - 1)/2 + humanPyramid(row - 1, column)/2)
    # Row -1 ,and Column -1 is because it trace back to the above row. Then divided by 2 which mean --
    # that position was split in two and spread down to 2 people. (move up and move back)
    # Only Row -1 mean only move up one row with the same column then divided by 2.
    # It will be recursive until it hit False statement


def user_repettion():
    """ Ask User whether they want to continue with another position."""

    while True:
        ask_user = input('Do you want to check on other position? [yes/no]: ').lower()
        if ask_user != 'yes' and ask_user != 'no':
            print('This is a wrong answer, please answer only "yes" or "no".')
        else:
            return ask_user


def main():
    """Introduction fucntion
    First, filter from the input that will not allow the user to input out of range pair(Invalid Pair).

    Second, humanPyramid function take row,column value and find the weight of that person by doing recursive."""

    intro()
    ans = 'yes'
    while ans == 'yes':
        row,column = input_user()
        print(humanPyramid(row,column) - 128 , 'pounds')
        ans = user_repettion()


if __name__ == '__main__':
    main()



