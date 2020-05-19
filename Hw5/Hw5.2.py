# Paripon Thanthong
# Date : 05/08/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/J6KRL1_TBig

# Cup and Dice Game
# Program Instruction

# 1.	Greet the user and ask their name.
# 2.	Provide the user with a balance of 100 dollars.
# 3.	Ask them if they would like to play a game.
# 4.	Generate a random number between 1 and 100.  This number will be called the goal.
# 5.	Ask the user how much they would like to bet.  This money is deducted from their account.
# 6.	Ask the user how many of each die they would like to roll.
# 7.	Create a cup filled with dice according to the user’s input.
# 8.	Roll the cup and display the results.
# 9.	If the roll exactly matches the goal, the user receives 10x bet added to their balance.
# 10.	Otherwise, if the roll is within 3 of the goal but not over, the user receives 5x bet added to their balance.
# 11.	Otherwise, if the roll is within 10 of the goal but not over, the user receives 2x bet added to their balance.
# 12.	Report the results to the user.  The message should include their name and updated balance.
# 13.	Ask if they would like to play again.  If so, go to step 4.

from Hw5_1 import *
def greeting():
    """ Greeting User and ask their Name"""

    print(""" Welcome to the Cup and Dice Game !!!""")

    u_name = input('Please type you name here to get start: ')

    return u_name

def user_balance_acc():
    """ Balance for 100$ """
    return 100

def ask_user():
    """Ask User whether they want to play or not"""

    while True:
        question = input('Do you want to play the game? [yes,no]: ').lower()
        if question != 'yes' and question != 'no':
            print('This is not the right answers, Please tryp only "yes" or "no"')
        else:
            return question

def goal():
    """Target number from 1 to 100"""

    rand_100 = random.randint(1,100)
    return (rand_100)

def user_bet():
    """The money user want to bet"""

    while True:
        try:
            u_bet = int(input('How much you want to bet on this game: $ '))
            if  u_bet <= user_balance_acc() and u_bet > 0 :
                return u_bet
            else:
                print('Try another number! Or put more money into you account.')
        except ValueError:
            print('This is not valid Value.')

def num_dice():

    """User choose how many dice on each type of dice they want to play"""

    while True:
        try:
            six_side = int(input('How many six sides die you want to roll?: '))
            ten_side = int(input('How many ten sides die you want to roll?: '))
            twenty_side = int(input('How many twenty side die you want to roll?: '))
            if (six_side + ten_side + twenty_side) >= 1:   # This prevent empty cup.
                return six_side, ten_side, twenty_side
            else:
                print('There is no dice in the Cup!, Select at least one Die')
        except ValueError:
            print('This is not a Valid value.')

def roll_cup():
    """ Roll the desire dice in the cup and show the result (total number of value) """

    six,ten,twenty = num_dice()
    cup = Cup(six,ten,twenty) # Create Cup

    cup.roll()  # Roll
    result = cup.getSum()
    #print(result)
    return result

def play_again():
    """Ask user whether they want to play more games or not."""

    while True:
        ask_user = input('Do you want to play more games? [yes,no]: ').lower()
        if ask_user != 'yes' and ask_user != 'no':
            print('This is not the right answers, Please try only "yes" or "no"')
        elif ask_user == 'yes':
            return ask_user
        else:
            print('See You Next Time!')
            break

def balance_calculation(roll,goal_target,money_bet,user_balance):

    """Check the value of the roll whether the user get a reward or not. And, update user balance."""
    print('This is your total number:',roll)
    print('This is the goal:',goal_target)
    if roll == goal_target:                                 #Exact match
        reward = 10 * money_bet
        user_balance = user_balance - money_bet + reward
        print('You won!')
    elif roll in range(goal_target + 1)[-3:]:               #Match range of 3 below the target
        reward = 5 * money_bet
        user_balance = user_balance - money_bet + reward
        print('You are partially won')
    elif roll in range(goal_target + 1)[-10:]:              #Match range of 10 below the target
        reward = 2 * money_bet
        user_balance = user_balance - money_bet + reward
        print('You are partially won')
    else:                                                   #No match
        user_balance = user_balance - money_bet
        print('You lose this game!')

    return user_balance  # Update Balance


def main():
    name = greeting()                   # Greting and Asking Name
    first_ask = ask_user()              # Ask User

    if first_ask == 'no':               # Check Answer from User
        return False                    # Stop Function

    user_balance = user_balance_acc()   # Initial set of balance for user
    print('\nHere is your free credit on the house!: ',user_balance,'$')

    ans = 'yes'
    while ans == 'yes' and user_balance > 0:
        goal_num = goal()

        print("Let's get started!")
        print('This is goal number for this game',goal_num,'!','\n')

        money_bet = user_bet()          # set user money bet
        roll = roll_cup()               # Roll Cup

        print("Here is your number!!", roll, '\n')
        user_balance = balance_calculation(roll,goal_num,money_bet,user_balance)  # User Balance will update after check result

        print(name,'This is your update balance:',user_balance,'$')
        if user_balance == 0:
            print("You don't have money!. See You Next Time")
            break
        ans = play_again()


if __name__ == '__main__':
    main()














