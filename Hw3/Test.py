def goldbach_test(number):
    list_prime = prime_list(number)
    result = ''
    for i in list_prime:
        for j in list_prime :
            if i+j == number and (i<j or i == j):
                result = str(number) + '=' +str(i) + '+' + str(j)
                print(result)


def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if(n%x) == 0:
                return False
        return True


def prime_list(num):
    '''Create a list of prime'''
    prime_lst = []
    for x in range(2 , num+1):
        if prime(x):
            prime_lst.append(x)
    return prime_lst

def main():
    num = range(4,101,2)
    for i in num:
        print(goldbach_test(i))


if __name__ == '__main__':
    main()

