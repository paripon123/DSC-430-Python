# Paripon Thanthong
# 04/07/2020
# "I have not given or received any unauthorized assistance on this assignment"
# Video link : https://www.youtube.com/watch?v=JZFlANGnU9w&feature=youtu.be

# Check if 2 number are coprime
def coprime(num_1,num_2):

    while num_2 != 0:           # 1 Check if num_2 = 0
        temp = num_1            # 2 Make substitution temp = num_1 and num_2 = temp % num2
        num_1 = num_2
        num_2 = temp % num_2    # 3 if num_2 != 0 go back to step 1 until num_2 == 0
    #print(num_1 == 1)
    return num_1 == 1

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
        next_pair = input("Do you want to try another pair [Yes/No]: ")
        if next_pair != "Yes":
            var = False
        #print(coprime(num_1,num_2))

    #print message and result(coprime or not coprime)


def main():
    #coprime(num_1,num_2)
    coprime_test_loop()
if __name__ == '__main__':
    main()