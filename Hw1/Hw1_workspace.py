# Paripon Thanthong
# 04/02/2020
# "I have not given or received any unauthorized assistance on this assignment"

# Code improvement
# 1. put question in to an array []
# 2. set while condition
# 3. text = input(x[counter])
# 4. if else condition --- If yes, counter +1 mean next index else break.

def grad_logic():
    score = 0
    file = input("Did student submit single uncompressed file: ")
    if file != 'Yes':
        print(score)
        return score
    author = input("Did student include the Author's name and date: ")
    if author != 'Yes':
        print(score)
        return score
    statement = input("Did student include honor statement: ")
    if statement != 'Yes':
        print(score)
        return score
    video = input("Did student include unlisted Youtube: ")
    if video != 'Yes':
        print(score)
        return score
    correctness = int(input('Correctness Score 0-3: '))
    elegance = int(input('Elegance Score 0-3: '))
    hygiene = int(input('Hygiene Score 0-2: '))
    discuss = int(input('Discussion Score 0-2: '))

    submission = input("Did student submit assignment on time: ")
    score = correctness + elegance + hygiene + discuss
    if submission == 'Yes':
        print(score)
        return score
    else:
        hour = int(input("How many hours late: "))
        score = score - (score * (hour/100))
        print(score)
        return score

# Fix coprime function
def coprime(num_1,num_2):
    #Check if 2 number are coprime
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    #print(num_1)
    return num_1

def coprime_test_loop():

    var = True
    while var:
        num_1 = int(input("Enter First Number: "))
        num_2 = int(input("Enter Second Number: "))

    # Ask user for 2 numbers
    # Pass the number to coprime function
    # 2 numbers are co-prime if the GDC(Greatest Common Divisor) is equal to 1.

        result = coprime(num_1,num_2)

        # Print hightest prime number from 2 number
        print(result)
        if result == 1:
            print("The pair of number are co-prime")
        else:
            print("The pair of number are not co-prime")

        # Only answers Yes to go forward.
        next_pair = input("Do you want to try another pair: ")
        if next_pair != "Yes":
            var = False
        #print(coprime(num_1,num_2))

    #print message and result(coprime or not coprime)


# For control structure
def main():
    #grad_logic()
    coprime_test_loop()


if __name__ == '__main__':
    main()