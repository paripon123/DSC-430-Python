# Paripon Thanthong
# Date : 04/21/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/2f2Dp7kcgzk

## Create Happy Function

## Work Flow

# 1. Create function to check number whether it is a happy number or not.
# 1.2 It needs sum square function.
def intro():
    """Introduction to the Program"""
    print("""
    'Happy', This is the program that output whether the number that user input
    is a happy number or not. It also indicates the type of number that user input is a prime or not.
    """)


def user_input():
    """Fucntion that take number input from USER."""
    while True:
        try:         # This try and except block is for catching error or inappropriate value.
            input_number = int(input("Enter number: "))
            if input_number > 0:            # Prevent input that is less than zero which cause error.
                return input_number
            else:
                print('Try another number.')
        except ValueError:
            print('This is not a number.')


def next_number():
    """Fucntion that ask user whether they want to check another number or not."""

    input_ans = ''
    while (input_ans != 'YES' and input_ans != 'NO'):
        input_ans = input("Do you want to check other number (Yes/No): ").upper()
    return input_ans


def happy_number_result(n):
    """Function that print the result based on the input
    prime,non-prime and happy or sad number."""

    if prime(n) and is_happy_number(n):
        print('This is a happy prime.')
    if prime(n) and not is_happy_number(n):
        print('This is a sad prime.')
    if not prime(n) and is_happy_number(n):
        print('This is happy non-prime.')
    if not prime(n) and not is_happy_number(n):
        print('This is sad non-prime.')


def is_happy_number(num):
    """ Check the whether number is a happy number or not """
    num_list = []
    while num != 1:                              # If input is 1 stop return true and stop function.
        #num = sum(int(i)**2 for i in str(num))  # It will iterate through string of input one by one.
        num = calculation(num)
        if num in num_list:                      # if it find the number in the list mean it's looping.
            return False
        num_list.append(num)                     # If not found append the number in bracket.
    return True

def calculation(num):
    """ This is the fucntion that do the calculation."""
    lst=[]
    for i in str(num):
        num_sqrt = int(i) ** 2
        lst.append(num_sqrt)
    sum_num = sum(lst)
    return sum_num


def prime(n):
    ''' Check whether the number is a prime or not. '''

    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if(n%x) == 0:
                return False
        return True


def main():
    intro()
    ans = 'YES'
    while ans == 'YES':            # For the looping the process purpose.
        num = user_input()
        happy_number_result(num)
        ans =  next_number()


if __name__ == '__main__':
    main()