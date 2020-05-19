# Paripon Thanthong
# Date : 02/05/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/51RMjwfa_D8

## Goldbach Deuce

##Work Flow
# 1. Ask user for i (list of random number) and n (given number)
# 2. binary search check whether there is a pair of number in this list sum to n (given number)
# 3. Restriction on target input for only even number.

def user_input():
    """User Input range of random number of list"""
    """User Input for the target number they expect from sum of a pair in random list of number"""

    # Try and Except for user Input.
    # Not allowed number in the list over 100 numbers.
    # Allowed only even target number.
    while True:
        try:
            input_num = int(input("Enter the amount numbers you want for the experiment: "))
            user_target = int(input("Enter the target number you expect from  calculation: "))
            if input_num > 100:
                print('This is out of range, try number that is not over 100.')
            elif user_target % 2 != 0:
                print('This is not an even number, please enter only even number.')
            else:
                return input_num,user_target
        except ValueError:
            print('This is not a number. Please re-enter only number as an integer.')
        except:
            print('There might be other issues, please try another numbers.')



def random_list(i):
    """Random list of number from 0 - 100"""

    import random
    num_list = sorted(random.sample(range(0, 100), i))
    return num_list


def user_repettion():
    """ Ask User whether they want to continue with another position."""

    while True:
        ask_user = input('Do you want to check on other position? [yes/no]: ').lower()
        if ask_user != 'yes' and ask_user != 'no':
            print('This is a wrong answer, please answer only "yes" or "no".')
        else:
            return ask_user


def sum_pair_search(lst, number):
    """This is the function that do the binary search and the prove the calculation"""

    # The list must be sorted!! Important!!!!
    num_lst = random_list(lst)
    for num in num_lst:             # O(n)
        low = 0                     # index of the lowest number
        high = len(num_lst) - 1     # index of the highest number

    # Binary search  O(log N)
        while low <= high:
            mid = (low + high) // 2
            if num + num_lst[mid] == number:    # Check if the pair are added up to the target number.
                print('Found It!')
                print(num, '+', num_lst[mid], '=', number)
                return True
            elif number < num_lst[mid]:         # Adjust high : Go search lower half portion
                high = mid - 1
            elif number > num_lst[mid]:
                low = mid + 1                   # Adjust low : Go search upper half portion
        print('No Pair Found in this Particular list of number.')
        return False


def main():
    """ Take input from user and provide to sum_pair_search to do the calculation."""

    ans = 'yes'
    while ans =='yes':
        num,target_num = user_input()
        sum_pair_search(num,target_num)
        ans = user_repettion()

    """ Try to count how many random times it will find the pair"""
    #count = 0
    #while sum_pair_search(num,target_num) == False:
    #    count +=1
    #print(count+1, 'random times until get the pair.')


if __name__ == '__main__':
    main()







