# Paripon Thanthong
# Date : 03/21/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/Q_tuWZ0gZDY

# Goldbach's Conjecture : is a theory about even number is a sum of two prime numbers.
# Test Goldbach's for 100 integers
# Note 1 is not prime


#### Flow Chart work
# Create a list of prime number
# test number with a sum of 2 prime number by using its list of prime.
# In main(), test with even number from 4 to 100

def intro():
    """Introduction"""

    print("""This is Goldbach's Conjecture program and test even number within range of 4 to 100.""")


def goldbach_test(number):
    ''' Test sum of 2 prime numbers '''
    list_prime = prime_list(number)
    #result = ''
    for i in list_prime:
        for j in list_prime:
            if i + j == number and (i < j or i == j):    # Condition that check how many prime can add up to input.
                                                         # 'and' condition will not allow to print the same pair.
                result = str(number) + '=' + str(i) + '+' + str(j)
                print(result)


def prime(n):
    ''' Check whether the number is a prime or not. '''

    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if (n % x) == 0:
                return False
        return True


def prime_list(num):
    '''Create a list of prime'''

    prime_lst = []
    for x in range(2, num + 1):  # start from 2 b/c of 1 is not prime.
        if prime(x):             # Call fucntion prime() to check each number whether it is a prime number or not.
            prime_lst.append(x)
    return prime_lst


def main():
    intro()
    num = range(4, 101, 2)       # Test number.
    for i in num:                # Loop through even number from 4-98
        goldbach_test(i)


if __name__ == '__main__':
    main()
